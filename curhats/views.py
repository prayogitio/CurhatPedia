from django.shortcuts import render, redirect, render_to_response
from .models import Post, Comment
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse
import json
from django.core import serializers
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required(login_url="/accounts/login")
def curhat_list(request):
    post_form = forms.CreatePost(request.POST)
    comments = Comment.objects.all().order_by('-date')
    comment_form = forms.CreateComment(request.POST)
    comments_count = {}
    
    post_list = Post.objects.all().order_by('-date')
    paginator = Paginator(post_list, 7)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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
            get_instance.post_id_id = id
            get_instance.save()
            return redirect('curhats:list')
    
@login_required(login_url="/accounts/login")
def like_post(request):
    if request.is_ajax():
        post_id = request.POST.get('post_id[]')
        print(post_id)
        msg = {
            'is_updated': Post.objects.filter(id=post_id).update(likes=F('likes')+1),
            'result_like': Post.objects.get(id=post_id).likes
        }
        return JsonResponse(msg)

@login_required(login_url="/accounts/login")
def profile_view(request):
    return render (request, 'curhats/profile.html', { 'user':request.user })