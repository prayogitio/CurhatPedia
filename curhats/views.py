from django.shortcuts import render, redirect
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login")
def curhat_list(request):
    post_form = forms.CreatePost(request.POST)
    posts = Post.objects.all().order_by('-date')
    return render(request, 'curhats/curhat_page.html', { 'post_form':post_form, 'post_data':posts })

@login_required(login_url="/accounts/login")
def create_curhat(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            get_instance = form.save(commit=False)
            get_instance.author = request.user
            get_instance.save()
            return redirect('curhats:list')