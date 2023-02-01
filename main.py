from fastapi import FastAPI, WebSocket
import random

# Create application
app = FastAPI(title='inide WebSocket')

@app.websocket("/eventstore/connect")
async def websocket_endpoint(websocket: WebSocket):
    print('Accepting client connection...')
    await websocket.accept()
    while True:
        try:
             # Wait for any message from the client
            data = await websocket.receive_text()
            # Send message to the client
            resp = {'value': random.uniform(0, 1)}
            await websocket.send_text(f"Message text was: {data}")
            await websocket.send_json(resp)
        except Exception as e:
            print('Exception error message:', e)
            break
    print('Got disconnected!!!')