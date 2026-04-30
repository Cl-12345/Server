from django.shortcuts import render

from django.http import HttpResponse
from .models import Chatroom


def index(req):
    return render(req, 'chat/index.html', {'rooms': Chatroom.objects.all()})

def chat(req, roomname: str):
    if not Chatroom.objects.filter(Name=roomname):
        return render(req, 'error.html')
    return render(req, 'chat/chatroom.html', {'roomname': roomname})
