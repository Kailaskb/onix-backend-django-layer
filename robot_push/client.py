import asyncio
import websockets
import json

async def connect_and_receive_data():
    # Update with the IP address and port of your WebSocket server
    server_ip = "192.168.1.69"  # Replace with the actual IP address
    server_port = 19301  # Replace with the actual port

    uri = f"ws://{server_ip}:{server_port}/ws/robot/"

    async with websockets.connect(uri) as websocket:
        # Connect to the WebSocket
        print("Connected to WebSocket")

        # Send a specific command (e.g., '8819301') to trigger data sending on the server
        command = '8819301'
        await websocket.send(command)
        print(f"Sent command: {command}")

        # Continuously receive and print data from the server
        while True:
            response = await websocket.recv()
            print(f"Received data from server: {response}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_and_receive_data())
