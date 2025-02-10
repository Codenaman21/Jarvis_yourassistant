# Jarvis - Voice Command Assistant

Jarvis is a Python-based voice assistant that can recognize voice commands and perform various tasks such as searching Wikipedia, opening websites, playing music, sending emails, and more.

## Features
- Voice recognition using `speech_recognition`
- Text-to-speech conversion using `pyttsx3`
- Wikipedia search functionality
- Open frequently used websites (YouTube, Google, Stack Overflow, etc.)
- Play music from a predefined directory
- Report the current time
- Send emails using SMTP
- Execute custom scripts

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Required Dependencies
Run the following command to install the required Python libraries:
```bash
pip install pyttsx3 speechRecognition wikipedia
```

## Usage
1. Run the script:
```bash
python ai.py
```
2. The assistant will greet you and wait for your command.
3. Speak out commands such as:
   - "Search Wikipedia for Python programming"
   - "Open YouTube"
   - "Play music"
   - "Tell me the time"
   - "Send an email to [recipient]"
   - "Exit" to stop the assistant

## Email Functionality
To use the email feature, update the `sendEmail` function with your email credentials. It is recommended to use an app password for security instead of your actual password.

## Future Enhancements
- Add more voice commands
- Integrate AI-based responses
- Improve error handling
- Support multiple languages

## License
This project is licensed under the MIT License.

## Disclaimer
Use this software at your own risk. Do not store sensitive credentials directly in the script.

