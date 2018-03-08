from django.shortcuts import render, redirect
from .models import Post, Comment
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login")
def curhat_list(request):
    post_form = forms.CreatePost(request.POST)
    posts = Post.objects.all().order_by('-date')
    comments = Comment.objects.all().order_by('-date')
    comment_form = forms.CreateComment(request.POST)
    comments_count = {}
    for post in posts:
        c = Comment.objects.filter(post_id_id=post.id).count()
        comments_count[post.id] = c
    return render(request, 'curhats/curhat_page.html', { 'post_form':post_form, 'post_data':posts, 'comment_form':comment_form, 'comments':comments, 'comments_count':comments_count.items() })

@login_required(login_url="/accounts/login")
def create_curhat(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            get_instance = form.save(commit=False)
            get_instance.author = request.user
            get_instance.save()
            return redirect('curhats:list')

@login_required(login_url="/accounts/login")
def post_comment(request,id):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            get_instance = form.save(commit=False)
            get_instance.author = request.user
            post_id = Post.objects.get(id=id)
            get_instance.post_id = post_id
            get_instance.save()
            return redirect('curhats:list')