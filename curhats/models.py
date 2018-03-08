from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, default=None, on_delete=models.DO_NOTHING)
    body = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)