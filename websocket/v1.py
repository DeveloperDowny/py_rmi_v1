import asyncio
import random
import string
import websockets

async def send_random_text(websocket, path):
    while True:
        # Generate a random 6-character long text
        random_text = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        
        # Send the random text to the client
        await websocket.send(random_text)
        
        # Sleep for one second before sending the next random text
        await asyncio.sleep(1)

# Create a WebSocket server
start_server = websockets.serve(send_random_text, "localhost", 8765)

# Start the WebSocket server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
