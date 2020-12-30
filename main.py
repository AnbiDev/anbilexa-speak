import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = []
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'anbi' in command:
                command = command.replace('anbi', '')
                print(command)
    except:
        pass
    return command

def run_command():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    else:
        talk("I don't know what you saying!")

while True:
    run_command()