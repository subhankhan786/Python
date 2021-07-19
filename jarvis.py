#-----------------------------------------------IMPORTS USED IN THIS PROJECT ARE LISTED BELOW------------------------------------------------#

import JarvisAI
import requests
from requests.api import request
from win32com.client import Dispatch
import datetime
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import re
import JarvisAI
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
import psutil

obj = JarvisAI.JarvisAssistant()
#-----------------------------------------------THIS FUNCTION ENABLES JARVIS TO SPEAK----------------------------------------------------------#


def speak(str):
    speak = Dispatch("SAPI.SPvoice")
    speak.speak(str)


wishtime = datetime.datetime.now().strftime("%H:%M")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning Sir! It's {wishtime}")

    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon Sir! It's {wishtime}")

    else:
        speak(f"Good Evening Sir! It's {wishtime}")


def takeCommand():
#-----------------------------------------------IT TAKES COMMAND FROM THE USER AND EXECUTE TASK------------------------------------------------#

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
#--------------------------------------------JARVIS WILL TELL ABOUT WHATEVER YOU SAY USING WIKIPEDIA MODULE------------------------------------#
        if 'tell me about' in query:
            speak('Searching...')
            query = query.replace("tell me about", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to my search")
            print(results)
            speak(results)

#---------------------------------------------------------OPENING AND APPS SITES---------------------------------------------------------------#

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open settings' in query:
            speak("opening settings")
            os.startfile("%windir%\System32\Control.exe")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open(playmusiclist)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "E:\All Games\vs code\Microsoft VS Code\Code"
            os.startfile(codePath)

        elif 'open chrome' in query:
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)

        elif 'exit' in query:
            speak("exiting")
            exit()

#------------------------------------------JARVIS WILL TELL WHEATHER USING REQUESTS AND BS4 MODULES--------------------------------------------#

        elif 'temperature' in query:
            r = requests.get("https://www.google.com/search?q=temperature")
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current temperature is {temp}")

#--------------------------------------------------JARVIS WILL TELL DATE USING JARVIS MODULE---------------------------------------------------#

        elif re.search('date', query):
            date = obj.tell_me_date()
            print(date)
            speak(date)

#------------------------------------------------Jarvis will  activate recipe mode using WikiHow-----------------------------------------------#

        elif 'activate recipe mod' in query:
            speak("Mode activated")
            while True:
                speak("Tell me what you want to know about")
                how = takeCommand()
                try:
                    if "exit mod" in how or "close mod" in how:
                        speak("Mode deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sir I can't find this")

        elif 'play iron man favourite music' in query:
            speak("playing sir")
            imfm = "https://music.youtube.com/watch?v=pAgnJDJN4VA&feature=share"
            webbrowser.open(imfm)

#----------------------------------------JARVIS WILL SEARCH ANYTHING ON GOOGLE----------------------------------------#

        elif 'search google' in query:
            speak("sir please tell me what you want to search")
            googlesearchquery = takeCommand()
            googlesearch = requests.get(f"https://www.google.com/search?q={googlesearchquery}")
            googleseachdata = BeautifulSoup(googlesearch.text, "html.parser")
            googlesearchresults = googleseachdata.find("div", class_="BNeawe").text
            speak(googlesearchresults)
            break

#------------------------------------------jarvis find my location using python------------------------------------------#

        elif 'where we are' in query or 'where i am' in query:
            speak("Let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                ipurl = 'https://get.geojs.io/v1/ip/geo/' + ipAdd+'.json'
                geo_requests = requests.get(ipurl)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                print(
                    f"Sir, I think we are in {city} city of {country} country")
                speak(
                    f"Sir, I think we are in {city} city of {country} country")
            except Exception as e:
                print("Sir due to network issue I am not able to find location")

#-----------------------------------------JARVIS WILL SEARCH ANY THING ON YOUTUBE---------------------------------------#

        elif 'search youtube' in query:
            speak("Sir tell what you want to search on youtube")
            youtubesearchquery = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={youtubesearchquery}")
#-----------------------------------------------------TALLKING WITH JARVIS----------------------------------------------#

        elif 'good morning' in query:
            speak("Good morning sir")

        elif 'good afternoon' in query:
            speak("Good afternoon sir")

        elif 'good evening' in query:
            speak("Good evening sir")

        elif 'good night' in query:
            speak("Good goodnight sir")

        elif 'sorry jarvis' in query:
            speak("It's okay")

        elif 'hello jarvis' in query:
            speak("Hey sir!")

        elif 'what is your name' in query:
            speak("My name is Jarvis")

        elif 'what can you do' in query:
            speak("I can do many things like I can tell where we are, how to make food, open apps and sites, tell date and time, tell wheather and temperature and much more.")

        elif 'say hello' in query:
            speak("Hello sir!")    

        elif 'in which language you are written' in query:
            speak("I am written in python")

        elif 'what are you doing' in query:
            speak("Sir I am listenng you")   