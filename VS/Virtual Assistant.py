import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    speak("hello sir, I am your virtual assistant , how can i help you . ")  
    speak("To know more about me. Say what can you do") 
   # speak("The program is to design a virtual assitant that will help you in analysing the caliber of the system in a way that will be defined in the further section " )


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
        #print(e)    
        speak("sorry this task is not defined. please say a defined task ")  
        return "None"
    return query


def website():
    speak(" please tell the  website you want to visit ")
    site=takeCommand()+'.com'
    print(site)
    webbrowser.open(site)
    speak("opened")

def hindi():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='hi')
            print("you said",{query})

        except Exception as error:
            return "none"

        return query

def Transl():
    speak("what you want to translate")
    line= hindi()
    translate=Translator()
    result= translate.translate(line)
    text=result
    speak(text)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('itbsc2020@gmail.com', 'Bscit@2020')
    server.sendmail('itbsc2020@gmail.com', to, content)
    server.close()



def demo():
    
    wishMe()
    
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ' youtube' in query:
            webbrowser.open("youtube.com")
        elif 'exit' in query:
            webbrowser.close("tr")
        elif 'dsvv' in query:
            webbrowser.open("dsvv.ac.in")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")      

        
        elif 'Translate' in query:
              Transl()
            
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open spotify' in query:
            os.startfile("C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.170.610.0_x86__zpdnekdrzrea0\\Spotify.exe")

        elif 'play music' in query:
            music_dir = 'D:\\bh'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif'thank you' in query:
            speak('your most welcome sir ,now what else can i do for you')

        elif 'stop music' in query:
            os.system("taskkill /im wmplayer.exe")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'open website' in query:
            website()

        elif 'date' in query:
             strdate= datetime.datetime.now().strftime("%D")
             print(strdate)
             speak(f"DATE IS {strdate}")
        elif 'open code' in query:
            codePath = "C:\\Users\\user80\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'location' in query:
          location()
        
        
        elif 'what can you do' in query:
            speak("I can do following task . Play music, Open google, Wikipedia search, Open website , Open youtube, Tell you correct time")
            print("I can do following task .\n Play music \n Open google \n Wikipedia search\n Open website \n Open youtube\n Tell you correct time")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("please enter email in which you want to send  ")
                to = input("enter you mail")+"@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")    
        elif 'shutdown system' in query:
            speak("want to shutdown speak yes if not speak no")
            choice=takeCommand()
            if choice == 'no':
                 exit()
            elif 'yes' in choice:
                 os.system("shutdown /s /t 1")    
        elif 'ok bye' in query:
            speak("thank you . see you later")
            quit()

if __name__ ==  "__main__":
    demo()
