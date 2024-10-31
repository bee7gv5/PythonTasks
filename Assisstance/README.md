# Voice Assistant

## Overview
This project is a voice assistant developed in Python, capable of performing various tasks based on voice commands. The assistant can open applications, send emails, set reminders, play music, read Word documents, and provide the current time. This task was completed at [Institution Name].

## Features
- **Voice Recognition**: Utilizes the `speech_recognition` library to capture and interpret user commands.
- **Text-to-Speech**: Implements the `pyttsx3` library to enable the assistant to speak responses.
- **Task Automation**: Performs tasks like opening web browsers, applications, and sending emails based on voice commands.
- **Reminder Functionality**: Allows users to set reminders at specified intervals.
- **Music Playback**: Plays music from a specified directory.
- **Document Reading**: Reads text from Word documents using the `python-docx` library.
  
## Technologies Used
- Python 3.x
- `speech_recognition` - for capturing and recognizing voice commands
- `pyttsx3` - for text-to-speech conversion
- `webbrowser` - for opening web pages
- `os` - for interacting with the operating system
- `smtplib` - for sending emails
- `python-docx` - for reading Word documents

## Installation
To run this project, you'll need to have Python installed on your computer. Follow the steps below to set up the environment:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant

2. Install the required packages:
   ```bash
   pip install speechrecognition pyttsx3 python-docx

3. Make sure you have the necessary permissions for using your microphone.

## Usage
Run the assistant:
```bash
python assist.py
```

Speak commands to the assistant. Some example commands include:

"What is the time?"
"Open Google."
"Send email."
"Play music."
"Read document."
To exit the assistant, say "exit" or "stop".


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Sample solution for the Voice-Assisstance task from [codealpha](https://www.codealpha.tech)