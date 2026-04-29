from django.shortcuts import render

from django.http import HttpResponse
from .models import Chatroom

def error(req):
    return HttpResponse('<p>你来到了未知的区域</p>')

def index(req):
    return render(req, 'chat/index.html')

def chat(req, roomname):
    if not Chatroom.objects.filter(Name=roomname):
        return error(req)
    return render(req, 'chat/chatroom.html', {'roomname': roomname})
