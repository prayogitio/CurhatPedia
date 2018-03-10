from django.shortcuts import render
from .models import Chat
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse

# Create your views here.
def selectfriend_view(request):
    friends = User.objects.all().exclude(id=request.user.id)
    return render(request, 'select_friend.html', { 'friends': friends })

def chatroom_view(request,id):
    if request.method == 'GET':
        to = User.objects.get(id=id)
        chats = Chat.objects.filter(user_one=request.user.id, user_two=to.id) | Chat.objects.filter(user_one=to.id, user_two=request.user.id)
        return render(request, 'chat_room.html', { 'to':to, 'chats': chats })

def messages_view(request,id):
    if request.method == 'GET':
        to = User.objects.get(id=id)
        chats = Chat.objects.filter(user_one=request.user.id, user_two=to.id) | Chat.objects.filter(user_one=to.id, user_two=request.user.id)
        return render(request, 'messages.html', { 'to':to, 'chats': chats })

def send_view(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        to_id = request.POST.get('to_id')
        to_obj = User.objects.get(id=to_id)
        c = Chat(user_one=request.user, user_two=to_obj, message=msg)
        if msg != '':            
            c.save()
        
        return JsonResponse({ 'msg': msg })
    else:
        return HttpResponse('Request must be POST.')


def profile_view(request):
    return render(request, 'profile.html', { 'user': request.user })