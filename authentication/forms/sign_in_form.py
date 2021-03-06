"""Sign in form module.
"""
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class SignInForm(AuthenticationForm):
    """Sign in form class.
    """
    username = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'id': 'id_signin_email_input'
            }
        )
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'id_signin_password_input'
            }
        )
    )
