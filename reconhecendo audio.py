import speech_recognition as sr

#Lendo Arquivos de Audio com Sphinx#

recon = sr.Recognizer()

PATH = 'Fala.wav'
with sr.AudioFile(PATH) as source:
    audio = recon.record(source)

print(recon.recognize_sphinx(audio))