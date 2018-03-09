from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.context_processors import csrf
from . import forms

def login_view(request):
    if request.method == 'POST':
        form = forms.MyLogin(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('curhats:list')
    else:
        form = forms.MyLogin()
    return render(request, 'index.html', { 'login_form':form, 'regis_form':forms.MyRegis() })

def register_view(request):
    if request.method == 'POST':
        form = forms.MyRegis(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            return redirect('curhats:list')
    elif request.method == 'GET':
        form = forms.MyRegis()
    return render(request, 'index.html', { 'regis_form':form, 'login_form': forms.MyLogin() })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')