from django_rq import job

from .models import Label, Translation


@job
def process_files(lang, file_content):
    for label, transl in file_content.items():
        n_label, label_created = Label.objects.get_or_create(
            text=label)
        n_transl, transl_created = Translation.objects.get_or_create(
            label=n_label)
        setattr(n_transl, lang, transl)
        n_transl.save()
