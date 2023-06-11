from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        self.connected = False  # Inicialmente establecido como desconectado

    async def disconnect(self, close_code):
        self.connected = False  # Establecer como desconectado al cerrar la conexión

    async def receive(self, text_data):
        data = self.scope["session"]
        message = data.get('message', '')  # Obtener el valor de la clave 'message' o una cadena vacía si no está presente
        if message == "conectar":
            self.connected = True
        elif message == "desconectar":
            self.connected = False
        await self.send_status()

    async def send_status(self):
        # Enviar el estado de conexión al cliente
        status = "conectado" if self.connected else "desconectado"
        await self.send(text_data=status)
