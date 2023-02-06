from django.urls import path
from .api import *
urlpatterns = [
    path('login',LoginAPI.as_view()),
    path('signup', RegistrationAPI.as_view()),
    path('prof', MainUser.as_view()),
]