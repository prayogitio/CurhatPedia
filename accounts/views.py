from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.context_processors import csrf

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('curhats:list')
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

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')