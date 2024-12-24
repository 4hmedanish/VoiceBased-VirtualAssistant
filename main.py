import os
import random
from turtle import listen
import webbrowser
import pyautogui 
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import eel

eel.init('web')

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    """Speak out the provided audio string."""
    engine.say(audio)
    engine.runAndWait()
    eel.updateStatus(f"Assistant: {audio}")

def takeCommand():
    """Take voice command from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.updateStatus("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        eel.updateStatus("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        eel.updateStatus(f"You said: {query}")
    except Exception:
        eel.updateStatus("Say that again...")
        return "None"
    return query.lower()


@eel.expose

def startListening():
    """Starts a continuous loop for voice commands."""
    speak("Hello, how can I assist you today?")
    while True:
                query = takeCommand().lower()
                if "turn of" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "translate" in query:
                    from Functions.Translator import translategl
                    query = query.replace("translate","")
                    translategl(query)
                    
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "shutdown the system" in query:
                  speak("Shutting down the system...")
                  os.system("shutdown /s /t 1")

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                     

                elif "volume up" in query:
                    from Functions.keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                   from Functions.keyboard import volumedown
                   speak("Turning volume down, sir")
                   volumedown()
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "favourite" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                     webbrowser.open("https://www.youtube.com/watch?v=6wrED1dw4Eo")
                    elif b==2:
                     webbrowser.open("https://www.youtube.com/watch?v=roz9sXFkTuE")
                    elif b==3:
                     webbrowser.open("https://www.youtube.com/watch?v=HPsxxBhv9kc")

                elif "open" in query:
                    from Functions.Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Functions.Dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from Functions.SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from Functions.SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from Functions.SearchNow import searchWikipedia
                    searchWikipedia(query)
                

                elif "calculate" in query:
                    from Functions.Calculatenumbers import WolfRamAlpha
                    from Functions.Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                
                elif "temperature" in query:
                    search = "temperature in nagpur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in nagpur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "remember that" in query:
                   rememberMessage = query.replace("remember that","")
                   rememberMessage = query.replace("jarvis","")
                   speak("You told me to remember that"+rememberMessage)
                   remember = open("Remember.txt","a")
                   remember.write(rememberMessage)
                   remember.close()
                elif "what do you remember" in query:
                   remember = open("Remember.txt","r")
                   speak("You told me to remember that" + remember.read())

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                elif "sleep" in query:
                   speak("Going to sleep,sir")
                   exit()

# Start the Eel application
eel.start('index.html', size=(700, 500))