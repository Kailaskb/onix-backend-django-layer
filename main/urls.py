from django.contrib import admin
from django.urls import path, re_path, include

from robot_push.consumers import RobotConsumer

websocket_urlpatterns = [
    path('ws/robot/', RobotConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('robot_push.urls')),
]

# Add the WebSocket URL patterns
urlpatterns += websocket_urlpatterns
