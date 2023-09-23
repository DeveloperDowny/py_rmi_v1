import asyncio
import websockets

async def receive_random_text():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            random_text = await websocket.recv()
            print(f"Received: {random_text}")

# Run the WebSocket client to receive random text
asyncio.get_event_loop().run_until_complete(receive_random_text())
