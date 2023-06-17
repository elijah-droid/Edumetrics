from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


async def websocket_handler(room_name, message):
    await async_to_sync(channel_layer.group_send)(
        room_name,
        {
            'type': 'websocket.send',
            'text': message,
        }
    )
