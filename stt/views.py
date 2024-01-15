from django.shortcuts import render

# Create your views here.
import os
from django.http import JsonResponse
from google.cloud import speech_v1p1beta1 as speech
from rest_framework.decorators import api_view


@api_view(['POST'])
def stt(request):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'token/stt_token.json'
    client = speech.SpeechClient()

    audio_content = request.body  # assuming audio data is sent in the request body

    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',  # Change the language code as per your requirements
    )

    response = client.recognize(config=config, audio=audio)

    # Extract the transcribed text from the response
    transcriptions = [result.alternatives[0].transcript for result in response.results]

    # Return the transcriptions as JSON response
    return JsonResponse({'transcriptions': transcriptions})
