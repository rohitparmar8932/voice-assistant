# voice-assistant
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        talk('hey Rohit, chinky here')
        talk('how can i help you')
        with sr.Microphone() as source:
            print("listining....")
            voice = listener.listen(source)

            command = listener.recognize_google(voice)
            if "chinky" in command:
                command = command.replace('chinky',' ')
                print(command)
    except:
        pass
    return command


def run_chinky():
    command = take_command()
    print(command)
    if "play"in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace("who is", '')
        info =wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk(' i dont understand say it again')


while True:
    run_chinky()
