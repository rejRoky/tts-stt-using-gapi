# tts-stt-using-gapi

## Description
This is a simple python script that uses Google Cloud Speech-to-Text and Text-to-Speech APIs to convert text to speech and speech to text.

## Requirements
- Python 3.6+
- Google Cloud Speech-to-Text API
- Google Cloud Text-to-Speech API
- Google Cloud SDK
- PyAudio
- Pydub
- ffmpeg
- ffprobe
- google-cloud-storage
- google-cloud-texttospeech
- google-cloud-speech
- google-api-python-client
- google-auth-oauthlib
- google-auth-httplib2
- google-auth
- googleapis-common-protos
- six
- urllib3
- requests
- requests-oauthlib
- oauthlib
- setuptools
- wheel
- pip
- virtualenv

## Installation
1. Install Python 3.6+
2. Install Google Cloud SDK
3. Install PyAudio
4. Install ffmpeg and ffprobe
5. Install the required python packages
6. Create a Google Cloud Platform project
7. Enable the Google Cloud Speech-to-Text API and Google Cloud Text-to-Speech API
8. Create a service account
9. Download a private key as JSON
10. Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON file downloaded
11. Create a bucket in Google Cloud Storage
12. Upload the audio files to the bucket
13. Update the variables in the script
14. Run the script

## Usage
```
python tts-stt.py
```     

## References
- https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
- https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries
- https://cloud.google.com/speech-to-text/docs/async-recognize
- https://cloud.google.com/speech-to-text/docs/async-recognize#speech-async-recognize-gcs-python
- https://cloud.google.com/speech-to-text/docs/async-time-offsets
- https://cloud.google.com/speech-to-text/docs/async-recognize#speech-async-recognize-gcs-python

## Author
- [Rejaul Islam Roky]( https://www.linkedin.com/in/rejaulroky/)