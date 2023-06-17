from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Add the WebSocket connection to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the WebSocket connection from the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle received WebSocket messages
        # In this example, we simply broadcast the received message to all connected clients in the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'websocket.send',
                'text': text_data
            }
        )

    async def websocket_send(self, event):
        # Handle WebSocket send event
        # This method is called when a message is sent to the WebSocket group from any connected client
        text_data = event['text']

        # Send the message to the WebSocket
        await self.send(text_data)

    # Override the __init__ method to assign the room_name attribute
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None

    # Other methods and event handlers...
