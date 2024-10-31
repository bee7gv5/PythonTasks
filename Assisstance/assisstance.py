import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from docx import Document

# Initialize the recognizer and voice engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice assistant's properties
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Change index to choose a different voice

def speak(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to capture and recognize user's voice command."""
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")  # Debugging line
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""

def greet_user():
    """Function to greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I assist you today?")

def send_email():
    """Function to send an email."""
    try:
        speak("Please say the recipient's email address.")
        recipient = listen()
        
        speak("What is the subject of the email?")
        subject = listen()
        
        speak("What would you like to say in the email?")
        body = listen()
        
        # Email setup - replace with your own credentials
        email = "your_email@gmail.com"
        password = "your_password"
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, recipient, msg.as_string())
        
        speak("Email has been sent successfully.")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")
        print(f"Error: {e}")

def set_reminder():
    """Function to set a reminder."""
    speak("What should I remind you about?")
    reminder = listen()
    speak("In how many seconds should I remind you?")
    try:
        seconds = int(listen())
        speak(f"Reminder set. I will remind you in {seconds} seconds.")
        time.sleep(seconds)
        speak(f"Reminder: {reminder}")
    except ValueError:
        speak("I didn't understand the time. Please try again.")

def play_music():
    """Function to play music from a specified directory."""
    music_dir = "D:\Music"  # Set your music directory here
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music.")
    else:
        speak("No music files found in the directory.")

def read_word_document():
    """Function to read text from a Word document."""
    speak("Please provide the full path to the Word document.")
    doc_path = listen()
    
    try:
        doc = Document(doc_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        if text:
            speak("Reading the document:")
            speak("\n".join(text))
        else:
            speak("The document is empty.")
    except Exception as e:
        speak("Sorry, I couldn't read the document.")
        print(f"Error: {e}")

def check_time(command):
    """Function to check and speak the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def perform_task(command):
    """Function to handle and execute tasks based on user's command."""
    
    # Check for time commands
    time_commands = ["time", "what is the time", "what's the time", "tell me the time", "current time"]
    if any(phrase in command for phrase in time_commands):
        check_time(command)
    
    # Open Google command
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    # Search command
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please provide something to search for.")

    # Send email command
    elif "send email" in command:
        send_email()

    # Set reminder command
    elif "set reminder" in command:
        set_reminder()

    # Play music command
    elif "play music" in command:
        play_music()

    # Read document command
    elif "read document" in command:
        read_word_document()

    # Open Notepad command
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")

    # Exit command
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    # Unsupported command handling
    else:
        speak(f"I'm sorry, I didn't understand the command: {command}. Please try again.")

# Main program loop
if __name__ == "__main__":
    greet_user()
    while True:
        command = listen()
        if command:
            perform_task(command)
