import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again !")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleeping mode" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                    

                # conversations commands -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                elif "hello" in query:
                    speak("Hello Sir, How are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "what is your name" in query:
                    speak("My name is jarvis")
                elif "who are you" in query:
                    speak("I am your jarvis, how can i help you ?")
                elif "tell about yourself" in query:
                    speak("Hello! I am Jarvis, an AI language model developed by Varun Patil. I am based on the Python language, My main purpose is to assist your computer on your given vioce commands. Give me some command and see me how's i works.")
                elif "thank you" in query:
                    speak("Your welcome, sir")
                elif "good morning" in query:
                    speak("Good Morning, sir")
                elif "good afternoon" in query:
                    speak("Good Afternoon, sir")
                elif "good evening" in query:
                    speak("Good Evening, sir")
                elif "good night" in query:
                    speak("Good Night, sir")
                elif "am sleeping now" in query:
                    speak("Okay good night sweet dream and take care, sir")
                elif "what you can do for me" in query:
                    speak("I'm assist your computer on your voice command. For example, Am giving greet to you, openign apps and websites, tellign temperatuer weather time and date. if you want to know about me in details please read the readme text file, My developer upgrading more functions in upcomign time.")
                
                # Command of Open | Close Web or App --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                elif "open" in query:
                    from Dictapps import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapps import closeappweb
                    closeappweb(query)

                # Search commands Import from SearchNow.py --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                # Temperature and Weather --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
                elif "temperature" in query:
                    search = "temperature in pune"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "temperature in pune"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                
                elif "go to sleep" in query:
                    speak("Okay sir , am sleeping now, you can wake up me anytime")
                    exit()
                
                


