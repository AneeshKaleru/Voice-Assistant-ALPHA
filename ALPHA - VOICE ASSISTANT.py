import pyttsx3 #Module used for text to speech conversion
import speech_recognition as sr #pip install speechRecognition
import datetime
from datetime import date
import wikipedia #pip install wikipedia
import webbrowser 
import smtplib #Module for sending emails
import pyjokes 
import pywhatkit #It is used for playing videos on Youtube
import requests #Used for getting data from Url
import pyautogui #Used for taking and saving screenshots
#install PyAudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alpha. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('glgamer276', '$ug@m105')
    server.sendmail('glgamer276@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Code for searching content on Wikipedia
        if 'according to wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("according to wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'access youtube' in query:
            webbrowser.open("youtube.com")

        elif 'access google' in query:
            webbrowser.open("google.com")
        
        elif 'location' in query:
            res = requests.get('https://ipinfo.io/')
            # Receiving the response in JSON format
            data = res.json()
            # Extracting the Location of the City from the response
            citydata = data['city']
            # Prints the Current Location
            print(citydata)
            speak(citydata)

        elif 'weather' in query:
            res = requests.get('https://ipinfo.io/')
            # Receiving the response in JSON format
            data = res.json()
            # Extracting the Location of the City from the response
            citydata = data['city']
            # Prints the Current Location
            print(citydata)
            # Passing the City name to the url
            url = 'https://wttr.in/{}'.format(citydata)
            # Getting the Weather Data of the City
            res = requests.get(url)
            # Getting the results!
            print(res.text)

        elif 'search' in query:
            speak('Searching in google')
            new=2
            query=query.replace('search','')
            url='https://www.google.com/search?q='
            term=query
            webbrowser.open(url+term,new=new)

        elif 'the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)  
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            today = date.today()
            d2 = today.strftime("%B %d, %Y")
            print( d2)
            speak(f"Sir, the date is {d2}")
            
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to=input('Enter the gmail below') 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")    
        elif 'tell me a joke' in query:
            engine.setProperty("rate", 140) 
            k=pyjokes.get_joke()
            print(k)
            speak(k)

        elif 'screenshot' in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\Dell\Desktop\pic.png')
            speak('screenshot successfully taken ')

        elif 'play' in query:
            query=query.replace('play','')
            pywhatkit.playonyt(query)
            