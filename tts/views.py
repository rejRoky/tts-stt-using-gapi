from django.shortcuts import render

# Create your views here.
import os

from django.http import HttpResponse
from google.cloud import texttospeech_v1
from rest_framework.decorators import api_view


@api_view(['POST'])
def tts(request):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'token/tts_token.json'
    client = texttospeech_v1.TextToSpeechClient()

    text = request.body.decode('utf-8')  # extract text from request data

    synthesis_input = texttospeech_v1.SynthesisInput(text=text)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code='bn-in',
        ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE
    )

    voices = client.list_voices()  # call the list_voices method

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    audio_content = response.audio_content  # get audio content from response

    return HttpResponse(audio_content, content_type='audio/mpeg')
