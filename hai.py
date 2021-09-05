import random
import os
import pyttsx3
import youtube_dl
import speech_recognition as sr
import datetime
import wikipedia
import time
import webbrowser
import selenium
import requests
from bs4 import BeautifulSoup
import wolframalpha
import pyjokes
import json
import pygeoip
from ip2geotools.databases.noncommercial import DbIpCity
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
app=wolframalpha.Client("G25LT6-962KKJJWVR")
print("___________________________________***************JARVIS*************______________________________________________")
user=input("USER--ID  :",)  
if(user=="augu:7777"):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    def speak(text):
        engine.say(text)
        engine.runAndWait()
    

    def greet():
        hr=int(datetime.datetime.now().hour)
        if hr<12:
            print("good morning, Augustine")
            speak("good morning, Augustine")
        if hr>=12 and hr<=18:
            print("good afternoon, Augustine")
            speak("good afternoon, Augustine")
        if hr>18 and hr<=24:
            print("good evening, Augustine")
            speak("good evening, Augustine")

    greet()
    def command():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.............")
            r.adjust_for_ambient_noise(source)
            sound=r.listen(source)
        try:
            print("recognizing...............")
            query=r.recognize_google(sound,language="en-in")
            print("you said ",query)
        except Exception as e:
            print(e)
            print("say anything")
            return "None"
        return query    

    while True:
        query=command().lower()
        if 'youtube downloader' in query:
            url=input(str("enter url :",))
            ydl={}
            with youtube_dl.YoutubeDL(ydl)as Ydl:
                Ydl.download([url])
        if 'talk' in query:
            query=query.replace('talk','')
            speak(query)
        if 'wikipedia' in query:
            query=query.replace('wikipedia ','')
            result=wikipedia.summary(query,sentences=5)
            print(result)
            speak('according to wikipedia ')
            speak(result)
        if 'whats the time' in query:
            tim=datetime.datetime.now().strftime('%H:%M:%S')
            print(tim) 
            speak('sir the time is')
            speak(tim)   
        if 'open google' in query:
            webbrowser.open('https://www.google.com')
        if  'google' in query:
            query=query.replace('google ','')
            webbrowser.open('https://www.google.com/?#q='+query)
        if 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')   
        if 'play music' in query:
            n=random.randint(0,2)
            print(n)
            musdir='C:/Users/Boby/OneDrive/Desktop/bgm'
            song=os.listdir(musdir)
            print(song)
            os.startfile(os.path.join(musdir,song[n]))
        if 'play video songs' in query:
            n=random.randint(0,10)
            print(n)
            musdir='C:/Users/Boby/OneDrive/Desktop/you--music'
            song=os.listdir(musdir)
            print(song)
            os.startfile(os.path.join(musdir,song[n]))
        if "what's the temperature" in query:
            res=app.query(query)
            speak(next(res.results).text)
            print(next(res.results).text) 
        if "say a joke" in query:
            speak(pyjokes.get_joke())
        if "track using address" in query:
            ip=str(input("enter ip for tracking :"))
            response=DbIpCity.get(ip,api_key="free")
            print("your region is :{0}".format(response.region))
            print("your country is :{0}".format(response.country))
            print("your city is :{0}".format(response.city))
            print("your region is :{0}".format(response.longitude))
            print("your region is :{0}".format(response.latitude))
        if "phone details" in query:
            ph=input("enter phone number :",)
            chm=phonenumbers.parse(ph,"CH")
            print(geocoder.description_for_number(chm,"en"))
            ser=phonenumbers.parse(ph,"RO")