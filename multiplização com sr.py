import speech_recognition as sr

#multiplização de numeros atraves do comando de voz#

recon = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("informe os numeros que deseja multipliza:")
        audio = recon.listen(source)
        soma = recon.recognize_google(audio, language='pt')
        if soma =='fechar': break
        print("sua multiplicação: " + str(soma))
        print("Resultado: " + str(int(soma[0]) * int(soma[4])))
