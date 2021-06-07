from gtts import gTTS
from pygame import mixer
import os

#sintetização com gTTS#

voz = gTTS("sintetizando voz com python", lang = 'pt')
voz.save("voz1.mp3")

#mixer.init()
#mixer.music.load("voz.mp3")
#mixer.music.play()

os.system("voz1.mp3")

x = input("Digite algo para finalizar")