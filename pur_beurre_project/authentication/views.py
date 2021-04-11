from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from authentication.models import CustomUser
from authentication.forms import SignUpForm, SignInForm

# Create your views here.

def account(request):
    pass
#     user_session = UserSession()
#     if user_session.active:
#         context = {
#             'user_session':user_session
#         }
#         return render(request, 'authentification/account.html', context)
#     else:
#         return login(request)


def sign_up(request):
    """
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = CustomUser.objects.create_user(
                email=email,
                password=password1,
                first_name=first_name)
            # user = authenticate(email=user.email, password=user.password)
            # if user is not None:
            return HttpResponseRedirect(reverse('supersub:index'))
        else:
            context = {
                'form' : form
            }
            return render(request, 'authentication/sign_up.html', context)   
    else:
        form = SignUpForm()
        context = {
            'form' : form
        }
        return render(request, 'authentication/sign_up.html', context) 


def sign_in(request):
    """
    """
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_authenticated:
                    return redirect('supersub:index')
        else:
            context = {
                'form' : form
            }
            return render(request, 'authentication/sign_in.html', context)
    else:
        form = SignInForm()
        context = {
            'form' : form
        }
        return render(request, 'authentication/sign_in.html', context) 

