from django.urls import path
from .views import create_alarm
urlpatterns = [
    path('',create_alarm,name="create_alarm_view"),  
]
