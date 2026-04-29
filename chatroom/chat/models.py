from django.db import models
from zoneinfo import ZoneInfo


class Chatroom(models.Model):
    # ID = models.IntegerField('id', default=0)
    Name = models.CharField('room_name', max_length=20)
    Description = models.CharField('description', max_length=1024)
    # a = models.
    def __str__(self) -> str:
        return self.Name
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, unique=True) 
    def __str__(self) -> str:
        return '{:s} ({:s})'.format(self.username, self.nickname)

class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    SendTime = models.DateTimeField('sendtime')
    message = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        # print(self.SendTime.)
        return "{:s} ({:s})".format(str(self.user), self.SendTime.astimezone(ZoneInfo('Asia/Shanghai')).strftime(fr'%d/%m/%Y, %H:%M:%S'))
    
