import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 所有用户加入同一个聊天室，房间名固定为 "lobby"
        self.room_group_name = 'lobby'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # 离开房间
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 接收来自 WebSocket 的消息
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        # 广播给房间内所有人
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    # 处理群发消息
    async def chat_message(self, event):
        message = event['message']
        # 发送回 WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))