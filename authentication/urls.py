# pylint: disable=C0103
"""urls module.
"""
from django.urls import path

from .views.account_view import AccountView
from .views.sign_up_view import SignUpView
from .views.sign_in_view import SignInView
from .views.sign_out_view import SignOutView

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_out/', SignOutView.as_view(), name='sign_out'),
    path('account/', AccountView.as_view(), name='account'),
]
