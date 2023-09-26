import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour: int = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning,Sir")
    elif 12 <= hour <= 18:
        speak("Good Afternoon,Sir")

    else:
        speak("Good Evening,Sir")

    speak("Please tell me, How can I help you ?")

