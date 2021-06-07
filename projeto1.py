import  pyttsx3
from datetime import datetime

#programa de boas vindas#

agora = datetime.now()
nome = "tauan jorge "
hora = agora.hour
minutos = agora.minute

frase = " olá " + str (nome) + " seja bem vindo moleque, agora são " + str (hora) + " horas e " + str (minutos) + " minutos"

en = pyttsx3.init()
en.setProperty('rate', 125)
en.setProperty('volume', 1)
en.setProperty('voz', b'brasil')

en.say(frase)
en.runAndWait()