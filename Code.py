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
