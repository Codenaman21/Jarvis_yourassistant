from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib
import pyautogui  # For tab, window, zoom controls
import time

# === Initialize Speech Engine ===
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# === Speak Function ===
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# === Wish User ===
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey, I am Jarvis. How may I help you?")

# === Voice Input ===
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

# === Send Email ===
def sendEmail(to, subject, content):
    try:
        sender_email = 'your_email@gmail.com'
        sender_password = 'your_app_password'  # Use app password

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(content, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, message.as_string())
        server.quit()
        speak("Email has been sent successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
        speak("Sorry, I wasn't able to send the email.")

# === Exit Jarvis ===
def exitJarvis():
    speak("Okay, shutting down. Have a nice day!")
    print("Jarvis is shutting down...")
    sys.exit()


# === MAIN PROGRAM LOOP ===
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # === Basic Commands ===
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=5, auto_suggest=False)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.DisambiguationError as e:
                speak(f"The term {query} is ambiguous. Please be more specific.")
                speak(f"Did you mean {', '.join(e.options[:3])}?")
            except wikipedia.PageError:
                speak(f"Sorry, I couldn't find a Wikipedia page for {query}.")
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, something went wrong while fetching information.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = r'C:\Users\HP\Music'
            songs = os.listdir(music_dir)
            if songs:
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
                to = "receiver_email@example.com"
                subject = "Email from Jarvis"
                sendEmail(to, subject, content)
            except Exception as e:
                speak(f"Error: {e}")

        # === OS CONTROL COMMANDS ===

        elif 'switch tab' in query or 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
            speak("Switched to next tab")

        elif 'previous tab' in query or 'last tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            speak("Switched to previous tab")

        elif 'switch window' in query:
            pyautogui.hotkey('alt', 'tab')
            speak("Switching window")

        elif 'minimize window' in query:
            pyautogui.hotkey('win', 'down')
            speak("Window minimized")

        elif 'maximize window' in query:
            pyautogui.hotkey('win', 'up')
            speak("Window maximized")

        elif 'close window' in query or 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
            speak("Tab closed")

        elif 'zoom in' in query:
            pyautogui.hotkey('ctrl', '+')
            speak("Zooming in")

        elif 'zoom out' in query:
            pyautogui.hotkey('ctrl', '-')
            speak("Zooming out")

        elif 'reset zoom' in query:
            pyautogui.hotkey('ctrl', '0')
            speak("Resetting zoom level")

        elif 'exit' in query or 'quit' in query or 'stop' in query:
            exitJarvis()
