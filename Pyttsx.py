import  pyttsx3

#2.Sintetização com Pyttsx3#

#nova_velocidade = 50
en = pyttsx3.init()
en.setProperty('rate', 150)
en.setProperty('volume', 0.90)
en.setProperty('voice', b'brazil')
en.say("faaala zé ruela")

en.runAndWait()