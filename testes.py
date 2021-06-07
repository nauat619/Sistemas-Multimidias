import  pyttsx3

en = pyttsx3.init()

#2.Sintetização com Pyttsx3#

#nova_velocidade = 50
#while nova_velocidade <=300:
    #en.setProperty('rate', nova_velocidade)
    #en.say("testando velocidade")
    #en.runAndWait()
    #nova_velocidade = nova_velocidade + 50


novo_volume = 0.1
while novo_volume <=1:
    en.setProperty('volume', novo_volume)
    en.say("testando volume")
    en.runAndWait()
    novo_volume = novo_volume + 0.3


