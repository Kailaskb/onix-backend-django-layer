# main/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from robot_push.consumers import RobotConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    re_path(r"ws/robot/$", RobotConsumer.as_asgi()),
                ]
            )
        ),
    }
)