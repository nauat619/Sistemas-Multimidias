#utilizada para sintese de fala
import pyttsx3
#utilizada para reconhecimento de fala
import speech_recognition as sr
import os

#Sintese#
en  = pyttsx3.init()
en.say('olá tauan você gostaria de ouvir a de sempre?')
en.setProperty('voice', b'brazil') # definindo linguagem
en.setProperty('rate', 130) # definindo velocidade
en.setProperty('volume', 1) # definindo volume
en.runAndWait()

#Reconhecimento#
recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')
    #print(resposta)

#reprodução#
if resposta=='sim':
    en.say('OK, execultando sua musica...')
    en.setProperty('voz', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()

    os.system('voz.mp3')
elif resposta=='não':
    en.say('OK, não tocarei ela hoje, encerrando o programa')
    en.setProperty('voz', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()