from django.test import TestCase

from translates.models import Label, Translation


class LabelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Label.objects.create(text='the_same')

    def test_text_label(self):
        label = Label.objects.get(id=1)
        field_label = label._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')


class TranslationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        english_transl = "the same"
        spanish_transl = "ditto"
        label = Label.objects.create(text='the_same')
        Translation.objects.create(
            label=label,
            english=english_transl,
            spanish=spanish_transl)

    def test_label_label(self):
        translation = Translation.objects.get(id=1)
        field_label = translation._meta.get_field('label').verbose_name
        self.assertEqual(field_label, 'label')

    def test_english_label(self):
        translation = Translation.objects.get(id=1)
        field_label = translation._meta.get_field('english').verbose_name
        self.assertEqual(field_label, 'English')

    def test_spanish_label(self):
        translation = Translation.objects.get(id=1)
        field_label = translation._meta.get_field('spanish').verbose_name
        self.assertEqual(field_label, 'Spanish')
