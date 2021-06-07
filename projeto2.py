from gtts import gTTS
from pygame import mixer
import os.path

#leitor de texto#

diretorio = input("Digite o diretorio do seu texto:")
teste = os.path.isfile(diretorio)

if teste == True:
    print("O arquivo esta sendo carregado...")
    file_data = open(diretorio)
    file_data = file_data.read()
    print("salvando arquivo...")
    voz = gTTS(file_data, lang='pt')
    voz.save("voz.mp3")

    print("execultando...")

    mixer.init()
    mixer.music.load("voz.mp3")
    mixer.music.play()

else:
    print("o diretorio é invalido!")



