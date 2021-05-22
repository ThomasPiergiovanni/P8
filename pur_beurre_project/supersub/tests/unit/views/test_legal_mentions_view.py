from django.test import TestCase

from supersub.forms import NavbarSearchForm


class LegalMentionsViewTest(TestCase):
    """
    """
    def setUp(self):
        self.response = self.client.get('/supersub/legal_mentions/')

    def test_get_with_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_with_template(self):
        self.assertTemplateUsed(self.response, 'supersub/legal_mentions.html')
    
    def test_get_with_navbar_form(self):
        self.assertIsInstance(
            self.response.context['navbar_form'],
            NavbarSearchForm)