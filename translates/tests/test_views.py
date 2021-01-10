from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from translates.models import Label, Translation


class TranslationListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        transl_number = 35
        for idx in range(transl_number):
            label = Label.objects.create(text=f'the_same{idx}')
            english_transl = "the same"
            spanish_transl = "the same"
            Translation.objects.create(
                label=label,
                english=f'{english_transl}{idx}',
                spanish=f'{spanish_transl}{idx}')

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/translate/list/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('translation-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('translation-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'translates/translation_list.html')

    def test_pagination_is_30(self):
        response = self.client.get(reverse('translation-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['translation_list']) == 30)

    def test_lists_all_translations(self):
        response = self.client.get(f'{reverse("translation-list")}?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['translation_list']) == 5)


class TranslationUpdateViewTest(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        english_transl = "the same"
        spanish_transl = "ditto"
        label = Label.objects.create(text='the_same')
        Translation.objects.create(
            label=label,
            english=english_transl,
            spanish=spanish_transl)

    def test_uses_correct_template(self):
        url = reverse('translation-update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'translates/translation_form.html')

    def test_redirects_to_list_view_on_success(self):
        url = reverse('translation-update', kwargs={'pk': 1})
        response = self.client.post(url, {'english': 'the sames', 'spanish': 'dittos'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('translation-list'))


class IndexViewTest(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'translates/index.html')


class TranslationDownloadViewTest(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_uses_correct_template(self):
        response = self.client.get(reverse('translation-download'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'translates/translate_download.html')
