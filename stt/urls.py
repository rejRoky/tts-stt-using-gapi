from django.urls import path

from .views import stt

urlpatterns = [
    path('api/stt/', stt, name='stt'),
]
