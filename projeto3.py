import speech_recognition as sr
import os
#projeto abrindo agenda atraves do comando de voz#
print("Olá usuario, deseja abrir sua agenda?")

recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')

if resposta =="sim":
    print("abrindo agenda...")
    os.system(r'C:\Users\TAUAN.J\Desktop\arquivos\texto.txt')

elif resposta =="não":
    print("solicitação negada")