from django.urls import path
from .views import card

urlpatterns = [
    path('', card, name='card'),
]