import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import FormView

from .forms import TranslationFilesForm
from .models import Label, Translation


def index(request):
    return render(request, 'translates/index.html')


class TranslationFilesView(FormView):
    template_name = 'translates/translate_form.html'
    form_class = TranslationFilesForm
    success_url = reverse_lazy('translation-list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            english_file = request.FILES['english_file']
            spanish_file = request.FILES['spanish_file']
            file_paths = {
                'english': english_file.temporary_file_path(),
                'spanish': spanish_file.temporary_file_path(),
            }
            for lang, file in file_paths.items():
                with open(file, 'r', encoding='utf-8') as file_json:
                    try:
                        file_content = json.load(file_json)
                    except json.JSONDecodeError as e:
                        messages.error(request,
                                       f'{e.msg} in {lang} file at {e.lineno} line')
                        return self.form_invalid(form)
                    except UnicodeDecodeError:
                        messages.error(request, 'Wrong file(s)')
                        return self.form_invalid(form)
                    else:
                        try:
                            for label, transl in file_content.items():
                                n_label, label_created = Label.objects.get_or_create(
                                    text=label)
                                n_transl, transl_created = Translation.objects.get_or_create(
                                    label=n_label)
                                setattr(n_transl, lang, transl)
                                n_transl.save()
                        except (AttributeError, IndexError, TypeError, KeyError):
                            messages.error(request, 'Broken file(s)')
                            return self.form_invalid(form)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TranslationListView(LoginRequiredMixin, ListView):
    model = Translation
    paginate_by = 30

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(Q(english__iexact=F('spanish')) |
                       Q(english__iexact='') |
                       Q(spanish__iexact=''))
        return qs


class TranslationUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Translation
    fields = ['english', 'spanish']
    success_url = reverse_lazy('translation-list')
    success_message = 'Label was updated'


@login_required
def translation_download(request):
    transl_number = Translation.objects.count()
    context = {
        'translations_number': transl_number,
    }
    return render(request, 'translates/translate_download.html', context)


@login_required
def download_file(request):
    lang = request.POST.get('lang')
    qs = Translation.objects.values_list('label__text', lang)
    filename = 'en_us' if lang == 'english' else 'es'
    transl_data = json.dumps(dict(qs), ensure_ascii=False, indent='\t')
    response = HttpResponse(transl_data, content_type='application/json')
    response['Content-Disposition'] = f'attachment; filename="{filename}.json"'
    return response
