import pyttsx3
import random
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning !')
    elif hour>=12 and hour<18:
        speak('Good AfterNoon !')
    else:
        speak('Good Evening !')
    speak('I am, Jarvis sir ! How may i help you')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recongnizing. . .")
        query=r.recognize_google(audio,language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('say that agian please. . .')
        return 'None'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('karansharma2002ai@gmail.com','chorkakaamchori')
    server.sendmail('karansharma2002ai@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia...')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir='C:\\Users\\chavi\\Desktop\\python\\Projects\\song'
            songs=os.listdir(music_dir)
            print(songs)
            a=random.randint(0,2)
            os.startfile(os.path.join(music_dir,songs[a]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir,the time is {strTime}')

        elif 'to code' in query:
            codepath='C:\\Users\\chavi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'email to karan' in query:
            try:
                speak('What should i say?')
                content=takeCommand()
                to='karansharma.ai24@jecrc.ac.in'
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send the email at the moment")