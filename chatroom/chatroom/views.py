from django.shortcuts import render

def wel(req):
    return render(req, 'wel.html')

def error(req):
    return render(req, 'error.html')