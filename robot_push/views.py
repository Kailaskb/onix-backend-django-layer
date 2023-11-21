# robot_push/views.py

import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse


def send_to_channel(data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "robot_group",
        {"type": "robot_location", "data": data},
    )

def tcp_server(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            robot_id = data.get('robot_id')
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if robot_id is not None and latitude is not None and longitude is not None:
                # Process the data as needed
                # You can save it to the database or perform any other actions

                # Send data to the WebSocket consumer
                send_to_channel(data)

                return JsonResponse({'message': 'Robot location sent to WebSocket consumer'})
            else:
                return JsonResponse({'error': 'Invalid data provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# 1a2b3c4d