from django.shortcuts import render

from django.http import HttpResponse
from .models import Chatroom
from django.contrib.auth.decorators import login_required

def index(req):
    print(1)
    return render(req, 'chat/index.html', {'rooms': Chatroom.objects.all()})

@login_required
def chat(req, roomname: str):
    if not Chatroom.objects.filter(Name=roomname):
        print('chat error')
        return render(req, 'error.html')
    print(12)
    return render(req, 'chat/chatroom.html', {'roomname': roomname})
