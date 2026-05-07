from django.urls import re_path
from . import consumerd   # 相对导入

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumerd.ChatConsumer.as_asgi()),
]