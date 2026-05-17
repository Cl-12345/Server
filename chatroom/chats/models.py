from django.db import models
from zoneinfo import ZoneInfo
from django.contrib.auth.models import AbstractUser

class Chatroom(models.Model):
    # ID = models.IntegerField('id', default=0)
    Name = models.CharField('room_name', max_length=20, unique=True)
    Description = models.CharField('description', max_length=1024)
    # a = models.
    def __str__(self) -> str:
        return self.Name
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True) 
    def __str__(self) -> str:
        return '{:s} ({:s})'.format(self.username, self.nickname)

class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    SendTime = models.DateTimeField('sendtime')
    message = models.CharField(max_length=1024)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        # print(self.SendTime.)
        return "{:s} ({:s})".format(str(self.user), self.SendTime.astimezone(ZoneInfo('Asia/Shanghai')).strftime(fr'%d/%m/%Y, %H:%M:%S'))
    
