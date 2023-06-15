import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

from numpy.f2py.symbolic import Language

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning sir. I hope you are doing well today.")

    elif hour>=12 and hour<18:
        speak("Hi sir, good afternoon.")

    else:
        speak("Good evening sir.")

    speak("I am Jarvis. How may I help you today?")

import speech_recognition as sr

import speech_recognition as sr

def takeCommand():
    # It takes mic input from user and returns the output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # İşlemlere başlamadan önceki bekleme süresi
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="tr-TR")
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        print("Sorry sir, could you repeat?")
        return "None"
    except sr.RequestError as e:
        print("Speak service is not working right now; {0}".format(e))
        return "None"

    return query




if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching on Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Results was like that sir! I am listening to you for my next mission.")

        #elif "youtube" in query:
        #    codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"
        #    os.startfile(codePath)

        elif "instagram" in query:
            webbrowser.open("instagram.com")

        elif "youtube" in query:
            webbrowser.open("youtube.com") 

        elif "google" in query:
            webbrowser.open("google.com")

        elif "saat" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime} sir.")