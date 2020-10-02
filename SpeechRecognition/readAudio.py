import speech_recognition as sr

PATH = 'audio.wav'

arquivo = sr.Recognizer()

with sr.AudioFile(PATH) as source:

 audio = arquivo.record(source)

try:

     fala = arquivo.recognize_google(audio,language='pt-BR')

     print(fala)

except sr.UnkownValueError:
     print("Não entendi") 