from pocketsphinx import LiveSpeech

#Criando Script Live Speech tentando completar uma frase#

for phrase in LiveSpeech():

    print("Voce disse: " +str(phrase))
