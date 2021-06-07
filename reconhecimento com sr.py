import speech_recognition as sr

#reconhecimento de voz#

recon = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        recon.adjust_for_ambient_noise(source, duration=3)
        print("Diga algo")
        audio = recon.listen(source)
        print(recon.recognize_sphinx(audio))