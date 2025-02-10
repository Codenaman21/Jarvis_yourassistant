from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib

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

    speak("hey I am jarvis how may i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, subject, content):
    try:
        # Sender's email credentials (Use an app password if 2-factor authentication is enabled)
        sender_email = 'nsachdeva300@gmail.com'
        sender_password = 'your_password'  # Use an app password instead of the actual email password

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(content, 'plain'))

        # Establish the SMTP server connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = message.as_string()

        # Send the email
        server.sendmail(sender_email, to, text)
        server.close()

        speak("Email has been sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("Sorry, I wasn't able to send the email.")

def exitJarvis():
    speak("Okay, shutting down. Have a nice day!")
    print("Jarvis is shutting down...")
    sys.exit()  # Exit the program



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()  # Strip extra spaces

            try:
                results = wikipedia.summary(query, sentences=5, auto_suggest=False)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except wikipedia.DisambiguationError as e:
                speak(f"The term {query} is ambiguous. Please be more specific.")
                print(f"Suggested options: {e.options[:3]}")  # Show only 3 suggestions
                speak(f"Did you mean {', '.join(e.options[:3])}?")

            except wikipedia.PageError:
                print(f"PageError: The page for '{query}' does not exist.")
                speak(f"Sorry, I couldn't find a Wikipedia page for {query}.")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                speak("Sorry, an error occurred while fetching information.")


        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = r'C:\Users\HP\Music'  # Use raw string literal to handle backslashes
            songs = os.listdir(music_dir)
            if songs:
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found in the directory.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:/Users/HP/Desktop/Jarvis/Jarvis/code.py"
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                speak("The code file was not found.")

        elif 'email to' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 to = "email_of_reciever"  # Replace with actual recipient
                 subject = "Email from Jarvis"
                 sendEmail(to, subject, content)
             except Exception as e:
                 speak(f"Error: {e}")
                
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            exitJarvis()
            
