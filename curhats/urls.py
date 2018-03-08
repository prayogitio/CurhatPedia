from django.urls import path
from . import views

app_name = 'curhats'

urlpatterns = [
    path('', views.curhat_list, name="list"),
    path('post/', views.create_curhat, name="create"),
    path('<int:id>', views.post_comment, name="post_comment"),
]
