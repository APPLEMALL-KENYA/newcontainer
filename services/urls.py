from django.urls import path
from .views import services_view

urlpatterns = [
    path('', services_view, name='services'),
]
