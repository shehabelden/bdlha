from django.urls import path
from  .notifications import *
urlpattern=[
   path('',NotificationConsumer.as_asgi())
]