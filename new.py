import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
import wikipediaapi
import time

engine = pyttsx3.init('sapi5')     

voices = engine.getProperty('voices') 

engine.setProperty('voice',voices[0].id)          


def speak(audio):                                
    engine.say(audio)
    engine.runAndWait()                          

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

def takecommand():                               
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:                                            
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')  
        print(f'User said: {query}\n')

    except Exception as e :
        print('Say that again please...')      
        return 'None'  
    return query

if __name__ == '__main__' :                   
    while True:
        query = takecommand().lower()  
        if 'search google for' in query :
            print("What do you want to search for on Google?")
            query = takecommand()
            query = query.replace(" ", "+")
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)


        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'what is the time' in query :
            current_time = time.strftime("%I:%M %p")
            response = "The current time is " + current_time
            speak(response)
            print(response)

        elif 'what is your honesty parameter' in query:
            speak(f'90 percent?')


        elif 'exit' in query:
            speak('goodbye')
            quit()

            