from django.shortcuts import render

from django.http import HttpResponse

def index(req):
    return render(req, 'chat/index.html')

def chat(req, roomname):
    return render(req, 'chat/chatroom.html', {'roomname': roomname})
