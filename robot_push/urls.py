# robot_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/tcp_server/', views.tcp_server, name='tcp_server'),
]
