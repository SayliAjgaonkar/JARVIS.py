💬 Jarvis - Python Text Assistant

A simple text-based virtual assistant built in Python. Jarvis interacts through text commands and provides spoken feedback using the pyttsx3 text-to-speech engine. It can open popular websites such as Google, YouTube, Facebook, and LinkedIn, all from the command line.

🚀 Features

🧠 Text-based interaction — communicate with Jarvis through typed commands

🌐 Quick access to websites — opens Google, YouTube, Facebook, and LinkedIn

🛑 Clean exit — type exit anytime to stop the assistant


🧩 How It Works

Run the program.
Type jarvis to activate the assistant.
Once active, you can enter commands like:
open google
open youtube
open facebook
open linkedin

Type exit to stop the program.

🛠️ Requirements

Install the text-to-speech library:
pip install pyttsx3

(webbrowser is part of Python’s standard library.)

▶️ Usage

Run the script in your terminal or command prompt:
python jarvis.py


Example session:

Please type 'Jarvis' to activate...
Command: jarvis
Jarvis: Yes? How can I assist you?
Command: open youtube
Command received: open youtube

📂 Project Structure
jarvis/
│
├── jarvis.py       # Main assistant script
└── README.md       # Project documentation

📜 License
This project is licensed under the MIT License — free to use, modify, and distribute.

💡 Future Improvements
Add more websites and commands
Add conversation memory
Create a GUI-based version


MY CODE

import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    # Command processing based on the command string
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "exit" in command.lower():
        speak("Goodbye.")
        exit()  # Exit the program when "exit" is typed
    else:
        print("Jarvis: Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        # Get the wake word "Jarvis" and then process commands
        print("Please type 'Jarvis' to activate...")
        command = input("Command: ").lower()

        if command == "jarvis":
            print("Jarvis: Yes? How can I assist you?")
            while True:
                # Now, wait for an actual command after the wake word
                command = input("Command: ").lower()
                print(f"Command received: {command}")
                processCommand(command)
        elif command == "exit":
            speak("Goodbye.")
            break  # Exit the program
        else:
            print("Please type 'Jarvis' to activate.")
