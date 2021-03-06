# pylint: disable=W0212
"""Sign in view module.
"""
from django.shortcuts import render, redirect

from authentication.forms.sign_in_form import SignInForm
from authentication.management.authentication_manager import (
    AuthenticationManager
)
from supersub.views.custom_view import CustomView


class SignInView(CustomView, AuthenticationManager):
    """Sign in view class.
    """
    def __init__(self):
        super().__init__()
        self._data['redirect'] = 'supersub:index'
        self._data['render'] = 'authentication/sign_in.html'

    def get(self, request):
        """Sign in view method on client get request.
        """
        form = SignInForm()
        self._data['ctxt']['form'] = form
        return render(request, self._data['render'], self._data['ctxt'])

    def post(self, request):
        """Sign in view method on client post request. If the user is present
        and its autheticaion is successfull, the user is redirected to the
        index page. If any of those criteria is not met, the same page is
        rendered to the user.
        """
        self._logout(request)
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = self._authenticate(form.cleaned_data)
            if user is not None:
                self._login(request, user)
                return redirect(self._data['redirect'])
        self._data['ctxt']['form'] = form
        return render(request, self._data['render'], self._data['ctxt'])
