import json

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from translates.forms import TranslationFilesForm


class TranslationFilesFormTest(TestCase):

    def test_upload_json(self):
        test_json = json.dumps({'the_same': 'the same'})
        bb = bytes(test_json, encoding='utf8')
        test_file = SimpleUploadedFile('test_json.json', bb, content_type='json')
        form = TranslationFilesForm(
            files={'english_file': test_file, 'spanish_file': test_file})
        self.assertTrue(form.is_valid())
