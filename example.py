import speech_recognition as sr


# Funcao responsavel por ouvir e reconhecer a fala
def listen_microphone():
    # Habilita o microfone para ouvir o usuario
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a funcao de reducao de ruido disponivel na speech_recognition
        microphone.adjust_for_ambient_noise(source)
        # Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        # Armazena a informacao de audio na variavel
        audio = microphone.listen(source)
    try:
        # Passa o audio para o reconhecedor de padroes do speech_recognition
        phrase = microphone.recognize_google(audio, language='pt-BR')
        # Após alguns segundos, retorna a frase falada
        print("Você disse: " + phrase)
    # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnknownValueError:
        print("Não entendi")

for i in range(3):
    listen_microphone()
