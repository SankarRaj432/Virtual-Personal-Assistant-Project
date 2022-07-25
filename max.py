#code for the virtual personal assistant for windows

import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import webbrowser
import pywhatkit as kit
import subprocess
import ctypes
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Max: Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
                break
            except:
                print("Try Again")


while True:
    query = command().lower()  ## takes user command

    if 'name' in query:
        speak("I am max  ...Your Digital Employee! ")
    elif 'are you single' in query:
        answers = ['I am in a relationship with wifi', 'No, I love spending time thinking about my crush wifi']
        speak(random.choice(answers))
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with humans like you")

    ### time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print({time})
        speak({time})

    ## date
    elif 'date' in  query:
        date = datetime.date.today()
        speak(date)
        print(date)


    ### celebrity
    elif 'who is' in query or 'tell about' in query:
        query = query.replace('who is', "")
        print(wikipedia.summary(query, 2))
        speak(wikipedia.summary(query, 2))

    ### Joke
    elif 'joke' in query:
        My_joke = pyjokes.get_joke(language="en", category="all")
        print(My_joke)
        speak(My_joke)

    ### news
    elif 'news' in query:
        def trndnews():
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
            page = requests.get(url).json()
            article = page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                print(i + 1, results[i])
            speak("here are the top trending news....!!")
            speak("Do yo want me to read!!!")
            reply = command().lower()
            reply = str(reply)
            if reply == "yes":
                speak(results)
            else:
                speak('ok!!!!')
                pass


        trndnews()

    ### music

    elif 'music' in query:
        music_dir = 'E:\\music'
        songs = os.listdir(music_dir)
        song = random.randint(0, len(songs) - 1)
        print(songs[song])
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    ###youtube

    elif "play" in query:
        song = query.replace('play', '')
        speak('playing' + song)
        kit.playonyt(song)

     ### simple queries

    elif "who are you" in query:
        speak("i am max your personal assistant")

    elif "hello" in query:
        speak("Hello sir")

    elif "hai" in query:
        speak("Hai sir")

    elif 'how are you' in query:
        speak("I am fine,Thank you")
        speak("How are you Sir")
    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by DAGS(Dinil, Althaf, Govind, Sankar).")


    elif "why you came to world" in query:
        speak("Thanks to DAGS Team .Further it's a secret")

    ### Device Controls
    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

     ### open Youtube
    elif 'open youtube' in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    ### Open Google
    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    ### Locating a place in Google Map
    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("Locating")
        speak(location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    ### Automatic Whatsapp message sending by setting time
    elif 'message in whatsapp' in query:
        kit.sendwhatmsg("+918139833169", "Hello",23,8)

    ### Suspending the program for a given time
    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop MAX from listening commands")
        a = int(command())
        time.sleep(a)
        print(a)

    ### Write notes converting input voice
    elif "write a note" in query:
        speak("What should i write, sir")
        note = command()

        file = open('jarvis.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = command()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("%m-%d-%Y %T:%M%p")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show the text" in query:
        speak("Showing Notes")
        file = open("DAGS.txt", "r")
        print(file.read())
        speak(file.read(6))


    ### Exit
    elif "bye" in query:
        speak("Bye! and Have a nice day ! ")
        break

    ### Unidentified Voices
    else:
        speak("I don't understand what you are saying")
