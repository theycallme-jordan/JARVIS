import datetime

import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from YT_auto import MusicPlayer
from News import *
import randfacts
from Jokes import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("morning")
    elif hour>=12 and hour<16:
        return ("afternoon")
    else:
        return ("evening")
today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir, good "+wishme()+ ", I'm your voice assistant Speedy. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if all(keyword in text for keyword in ["what", "about", "you"]):
    speak("I am having a good day sir")

speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("Searching {} in Wikipedia".format(infor))
    print("Searching {} in Wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif all(keyword in text2 for keyword in ["play", "video"]):
    speak("You want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on YouTube".format(vid))
    print("Playing {} on YouTube".format(vid))
    chrome_driver_path = r"C:\Users\gusai\Driver\chromedriver.exe"
    assist = MusicPlayer(driver_path=chrome_driver_path)
    assist.play(vid)

    # input("Press Enter to close the browser...")

elif "news" in text2:
    print("Sure sir, now i will read news for you.")
    speak("Sure sir, now i will read news for you.")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure sir,")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)

elif "joke" in text2:
    speak("Sure sir, get ready for some jokes")
    ar=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

