import pyttsx3 #pip install pyttsx3
'''if you get audio error download pyaudio wheel file from unofficial bianry site'''
#https://www.lfd.uci.edu/~gohlke/pythonlibs/

'''from above site, please download file according to your python verion
#for me my python version is 3.8 & 32 bit so i downloaded 
#PyAudio‑0.2.11‑cp38‑cp38‑win32.whl'''
#cp38 is python version & win32 is 32bit
#then open powershell window where is your downloaded file and install it by using pip command

import datetime
import speech_recognition as sr #pip install speech_recognition
import os
import cv2 #pip install cv2
import random
from requests import get
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit as kit #pip install pywhatkit
import smtplib #pip install smtplib
import sys 
import pyowm #pip install pyowm 
import time 


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to wish 
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")

    elif hour>=12 and hour<=18:
        speak("good Afternoon sir!")

    else:
        speak("good Evening sir!")


    speak("I am jarvis.  tell me how may i help you")

#to send email here we create function below we write code
def sendEmail(to,content):
    server = smtplib.SMTP("smtplib.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("your email id", "your password")
    server.sendmail("your email id", to, content)
    server.close()

#speech to text
def takecommand():
    #it take microphoe input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listining.....")
        r.pause_threshold =1 #it allow to complete your sentence while taking breath for 1sec
        #it will not proceed command.gives you time to complete your command
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        cm=takecommand().lower()
        return cm
        
        return None
    return query #return query receive from user


if __name__ == "__main__":
    wishme() #every time wish you when you run jarvis
    while True:
        
        query=takecommand().lower()

        #logic building for task

        #to open notepad
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            
        #open adobe reader
        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32"
            os.startfile(npath)

        #open command prompt
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow('webcam', img)
                k =cv2.waitkey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        #play music available in your pc
        elif "play music" in query:
            music_dir = "C:\\Users\\Default\\Music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            #play random song from play list
            for song in songs:
                if songs.endwith(".mp3"):
                    os.startfile(os.path.join(music_dir,song))

        #this will show your computer ip address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP adress is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia for you sir....")
            query = query.replace("wikipedia","") #it delet wikipedia word from your query & search for remaining query
            results = wikipedia.summary(query,sentences=2) #store what you have search in result 
            #sentence=2 means how many sentences do you want to hear/print from jarvis.
            speak("According to wikipedia")
            print(results) #print the result
            speak(results) #speak the result

        #this is just for fun you can create your own
        elif "donald trump" in query:
            speak("he is a  dum boy")
            cm = takecommand().lower()
            speak("my apology sir")
            speak("he is ex-president of usa...,who served as the 45th president of the United States from 2017 to 2021.")
            
        
        #open youtube
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
         #open facebook
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        
        #open instagram
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/") #open your watsapp 
            speak("here you go ")

        elif "open google" in query:
            speak(" sir What should i search on google")
            cm = takecommand().lower() #speak what you want to search on google
            webbrowser.open(f"{cm}") #convert query in string


        elif "send message" in query:
            kit.sendwhatmsg("+91 your mobile number ", "this is a testing protocol",2,24)
            #you must be login in watsappweb on your desktop before using this query then you can close browser 
            '''first mobile number with country code in prefix,then message you want to send,then time(here 2 bajake 24sec)'''
            speak("message send succefully")

        elif "play song on youtube" in query:
            speak(" sir What should i play") #he ask you what you want to play
            cm = takecommand().lower() #tell the jarvis what you want to play
            kit.playonyt(f"{cm}") #convert query in to string and search query on youtube
        
        elif "email to rahul" in query:
            try:
                speak("what should i say") #ask what to write in mail
                content=takecommand().lower() #what you want to write in mail
                to = "gibin@gmail.com" #here email of person you want to send mail
                sendEmail(to.content)
                speak("Email has  been send to rahul")
            
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this messege")
        
        elif  "close" in query:
            speak("happy to help you sir, have a good day.")
            sys.exit() #it close all running programm start by jarvis 


        elif  "hello" in query:
            speak("hello sir please tell me how may i help you")
 
        #just for fun
        elif "command mode" in query: 
            speak("command mode activated")

        elif "upgrade" in  query:
            speak("checking for updates sir")
            time.sleep(1) #take pause for 1sec
            speak("upgrading myself please hold on") #speak this after 1sec
            time.sleep(1) #take pause for 1sec
            speak("5 second left to complete upgrade") #speak this after 1sec
            time.sleep(5) #take pause for 5sec
            speak("update completed sir...") #speak this after 5sec
            time.sleep(1)
            speak("hello sir i am jarvis. reloaded..... version two point O ..., Speed 1 tera hertz......, memory 1 gigabyte......")

        #after update you can aske below below query this make your jarvis cool 
        elif "who are you" in query:
            speak("i am jarvis. reloaded..... version two point O ..., Speed 1 tera hertz......, memory 1 gigabyte......")

        elif "sagar" in query:
            speak("wo lavde ka baal hai...")
            time.sleep(2)
            speak("do wana tell him")
        speak("do you have any other work sir") #it ask you if you want to open another task
        