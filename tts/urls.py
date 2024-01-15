from django.urls import path

from .views import tts

urlpatterns = [
    path('api/tts/', tts, name='tts'),

]
