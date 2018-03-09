from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms
from django.template.context_processors import csrf
from accounts import forms

def homepage(request):
    regis_form = forms.MyRegis()
    login_form = forms.MyLogin()
    return render(request, 'index.html', { 'regis_form': regis_form, 'login_form': login_form })

