from django.urls import path
from .api import *

urlpatterns = [
    path('Product', ProductApi.as_view()),
    path('', CategoriesApi.as_view())
]
