import speech_recognition as sr

def ouvir_microfone():

    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Fale qualquer coisa: ")

        audio = microfone.listen(source)

    try:

        fala = microfone.recognize_google(audio,language='pt-BR')

        print("Você falou: " + fala)

    except sr.UnkownValueError:
        print("Não compreendi o que você falou!")

    return fala

ouvir_microfone() 
