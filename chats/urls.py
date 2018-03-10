from django.urls import path
from . import views

app_name = 'chats'
urlpatterns = [
    path('', views.selectfriend_view, name="selectfriend"),
    path('send/', views.send_view, name="send"),
    path('profile/', views.profile_view, name="profile"),
    path('chatroom/<int:id>', views.chatroom_view, name="chatroom"),
    path('chatroom/messages/<int:id>', views.messages_view, name="getmessages")
]