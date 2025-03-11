# Import necessary libraries
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import os  # For system operations
import webbrowser  # For web browsing
import pyautogui  # For GUI automation (e.g., taking screenshots)
import time  # For time-related operations
import pyaudio  # For audio input (microphone access)

# Initialize PyAudio to check if it's working
p = pyaudio.PyAudio()
print("PyAudio is installed and working!")

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()  # Create a recognizer object
engine = pyttsx3.init()  # Initialize the text-to-speech engine

# Set properties for the voice
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to speak text
def speak(text):
    """
    Converts the given text to speech and speaks it out loud.
    """
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    """
    Listens to the user's voice input and converts it to text.
    Returns the recognized command as a string.
    """
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen to the user's voice
        try:
            command = recognizer.recognize_google(audio)  # Use Google's speech recognition API
            print(f"You said: {command}")
            return command.lower()  # Return the command in lowercase
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

# Function to handle commands
def handle_command(command):
    """
    Processes the user's command and performs the corresponding action.
    """
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "open browser" in command:
        speak("Opening browser.")
        webbrowser.open("https://www.google.com")  # Open Google in the default browser
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")  # Open Notepad
    elif "take screenshot" in command:
        speak("Taking a screenshot.")
        screenshot = pyautogui.screenshot()  # Capture the screen
        screenshot.save("screenshot.png")  # Save the screenshot as an image file
        speak("Screenshot saved.")
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")  # Shutdown the system after 1 second
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()  # Exit the program
    elif "lock screen" in command:
        speak("Locking the screen.")
        os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock the screen
    elif "play music" in command:
        speak("Playing music.")
        music_dir = "C:\\Path\\To\\Your\\Music\\Folder"  # Replace with your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song in the directory
    elif "what time is it" in command:
        current_time = time.strftime("%I:%M %p")  # Get the current time
        speak(f"The time is {current_time}")
    elif "search google for" in command:
        query = command.replace("search google for", "")  # Extract the search query
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")  # Open Google search results
    else:
        speak("I don't know that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am JARVIS. How can I assist you?")
    while True:
        command = listen()  # Listen for user input
        if command:
            handle_command(command)  # Process the command