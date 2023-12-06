# consumer.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import rclpy
from .subscriber import StatusDataSubscriber
from threading import Thread

rclpy.init()
minimal_subscriber_instance = StatusDataSubscriber()
minimal_subscriber = Thread(target=rclpy.spin, args=(minimal_subscriber_instance,), daemon=True)
minimal_subscriber.start()

# ... (import statements)

class RobotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.websocket_state = "CONNECTED"
        print("Client connected")
        self.send_continuous_data = False
        print(self.websocket_state)

        # asyncio.ensure_future(self.send_latest_ros_data_as_json())

    async def receive(self, text_data):
        try:
            if text_data == '8819301':
                print(f"Received text data: {text_data}")
                self.send_continuous_data = True  # Set the flag to True

            while self.send_continuous_data:
                # Access the get_latest_data method on the StatusDataSubscriber instance
                latest_data = None

                try:
                    latest_data = minimal_subscriber_instance.get_latest_data()
                except Exception as e:
                    print(f"Error getting latest ROS data: {e}")

                print(f"Latest ROS data: {latest_data}")

                if latest_data:
                    data_json = json.dumps(latest_data)
                    await self.send_data_to_client(data_json)
                    print(f"Sent data to client: {data_json}")

                await asyncio.sleep(0.01)

        except Exception as e:
            print(f"Error in receive: {e}")

    async def send_data_to_client(self, data):
        try:
            await self.send(text_data=json.dumps(data))
        except Exception as e:
            print(f"Error sending data to client: {e}")

    async def disconnect(self, close_code):
        try:
            await self.close()
            self.websocket_state = "DISCONNECTED"
            print("Client disconnected")
            self.send_continuous_data = False  # Stop sending data when the client is disconnected
        except Exception as e:
            print(f"Error in disconnect: {e}")

