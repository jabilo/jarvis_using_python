import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import googlesearch
from selenium import webdriver


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    
    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")


    speak("i am jarvis your a i assistant  sir please tell me how may i help you")

def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("listening.....")
        r.energy_threshold =3500
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing........")
        querry = r.recognize_google(audio,language="en-IN")
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)

        print("say that again please.....")
        return "None"
    return querry
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jabilo.2002@gmail.com', 'jabilojose#gmail')
    server.sendmail('jabilo.2002@gmail.com', to, content)
    server.close()
       
if __name__ == "__main__":    
    wishme()
    while True:
    # if 1:
        query = takecommand().lower()
        print(query)

        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("sorry there was an issue in searching")

        elif 'jarvis' in query:
            speak("yes sir tell me")
            info = takecommand()
            query = info
        
        

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        
        elif 'how are you' in query:
            speak("i am fine sir, what about you")
        
        elif 'boor'  in query:
            speak("i can tell you a joke then sir")
            speak("why do bees have sticky hair ?")
            speak("because they have honey comb")      

        elif 'my data' in query:
            speak("tell me about your self sir")
            speak("what is your name")
            name = takecommand()
            speak("ok")
            speak("what is your age?")
            age = takecommand()
            speak("ok")
            speak("what do you like to do")
            hobby = takecommand()
            speak("ok thats cool")
            speech = takecommand()
            if 'what did i say' in speech:
                say("you said your name is ",name,"and you are ",age,"years old and you like to ",hobby )
            else:
                speech("that is nice hearing from you sir")

        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com/in/")
        
        elif 'open java ide' in query:
            speak("opening java ide")
            webbrowser.open("C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2020.3.1\bin\idea64.exe")
        
        elif 'open code blocks' in query:
            speak('opening code blocks for programming')
            webbrowser.open("C:\Program Files\CodeBlocks\codeblocks.exe")

        elif 'open stackoverflow' in query:
            speak("opening stack over flow")
            webbrowser.open("stackoverflow.com")   
        
        


        elif 'play music' in query:
            music_dir = 'F:\music'
            songs = os.listdir(music_dir)
            print(songs)   
            speak("playing your favourite music")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "jabilo.2002@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend jabilo . I am not able to send this email") 
        elif 'google search ' in query:
            try:
                speak("what should i search in google ")
                gsearch = takecommand()
                for j in search(gsearch, tld="co.in", num=10, stop=10, pause=2): 
                    print(j) 
                    webbrowser.open(j)
                    break
            except Exception as e:
                print(e)
                speak("sorry there was an issue")

