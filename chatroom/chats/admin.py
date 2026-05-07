from django.contrib import admin

# Register your models here.
from .models import Message, Chatroom, User

admin.site.register(Message)
admin.site.register(Chatroom)
admin.site.register(User)
