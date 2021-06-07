#utilizada para sintese de fala
import pyttsx3
#utilizada para reconhecimento de fala
import speech_recognition as sr
import webbrowser

#Sintese#
en  = pyttsx3.init()
en.say('olá tauan o que você gostaria de pesquisar na web?')
en.setProperty('voice', b'brazil') # definindo linguagem
en.setProperty('rate', 130) # definindo velocidade
en.setProperty('volume', 1) # definindo volume
en.runAndWait()

#Reconhecimento#
recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')
    print(resposta)

#reprodução#
if resposta=='acessar google':
    en.say('OK, abrindo o google...')
    en.setProperty('voz', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()

    webbrowser.open('www.google.com')

elif resposta == 'acessar noticias':
    en.say('OK, acessando as noticias...')
    en.setProperty('voz', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()

    webbrowser.open('www.terra.com.br')

elif resposta == 'abrir youtube':
    en.say('OK, abrindo o youtube...')
    en.setProperty('voz', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()

    webbrowser.open('https://www.youtube.com/')

else:
    en.say('Desculpe comando não reconhecido...')
    en.setProperty('voz', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()