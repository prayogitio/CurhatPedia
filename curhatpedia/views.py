from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms
from django.template.context_processors import csrf

def homepage(request):
    regis_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'index.html', { 'regis_form': regis_form, 'login_form': login_form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect('test.html')
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', { 'login_form':form, 'regis_form':UserCreationForm() })

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            return redirect('test.html')
    elif request.method == 'GET':
        form = UserCreationForm()
    return render(request, 'index.html', { 'regis_form':form, 'login_form': AuthenticationForm() })