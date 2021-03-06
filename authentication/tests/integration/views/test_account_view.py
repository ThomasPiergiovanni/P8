# pylint: disable=C0116
"""Test account view module.
"""
from django.test import TestCase

from authentication.tests.unit.models.test_custom_user import CustomUserTest


class AccountViewTest(TestCase):
    """Test account view class
    """
    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()

    def test_get_with_redirect(self):
        response = self.client.get('/authentication/account/', follow=True)
        self.assertEqual(
            response.redirect_chain[0][0],
            '/authentication/sign_in/'
        )

    def test_get_with_render(self):
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/authentication/account/', follow=True)
        self.assertTemplateUsed(response, 'authentication/account.html')
        self.assertEqual(response.context['user'].email, 'testuser@email.com')
