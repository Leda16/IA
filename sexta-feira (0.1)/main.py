# Our main file.

from vosk import Model, KaldiRecognizer
import psutil, os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify

# Sintese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def evaluete(text):
    # Reconhecer entidade
    entity = classify(text)           
    if entity == 'time|getTime':
        speak(core.SystemInfo.get_time())
    elif entity == 'time|getDate':
        speak(core.SystemInfo.get_date())

    # Abrir programas
    elif entity == 'open|notepad':
        speak('Abrindo bloco de notas')
        os.system('notepad.exe')
    elif entity == 'open|opera':
        speak('Abrindo operaGX')
        os.system('"C:/Users/artur/AppData/Local/Programs/Opera GX/launcher.exe"')
    elif entity == 'open|fivem':
        speak('Abrindo fiveM')
        os.system('"C:/FIVEM/FIVEM/Fivem.exe"')
            
    print('Text: {} Entity: {}'.format(text, entity))
    speak(text)

# Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala

while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None: 
            text = result['text']
            evaluete(text)
           

            