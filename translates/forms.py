from django import forms
from django.core.validators import FileExtensionValidator


class TranslationFilesForm(forms.Form):
    english_file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.json'}),
                                   validators=[FileExtensionValidator(allowed_extensions=['json'])])
    spanish_file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.json'}),
                                   validators=[FileExtensionValidator(allowed_extensions=['json'])])
