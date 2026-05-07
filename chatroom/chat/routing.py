from django.urls import re_path
from . import consumers   # 相对导入

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]