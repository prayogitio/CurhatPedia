from django.shortcuts import render, redirect
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="accounts/login")
def curhat_list(request):
    post_form = forms.CreatePost(request.POST)
    return render(request, 'curhats/curhat_page.html', { 'post_form':post_form })

@login_required(login_url="accounts/login")
def create_curhat(request):
    pass