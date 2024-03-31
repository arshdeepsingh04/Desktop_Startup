# Importing required libraries
import pyttsx3  # pip install pyttsx3==2.71
import datetime
import psutil  # pip install psutil (for checking battery)
import socket
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from pandas import read_csv, DataFrame
import re

# Initializing text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 189)

# Function for text-to-speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to greet according to time
def wish():
    hour = datetime.datetime.now().hour
    tt = datetime.datetime.now().strftime("%I:%M %p")
    
    if 0 <= hour < 12:
        speak(f"Good morning sir, it's {tt}")
    elif 12 <= hour < 17:
        speak(f"Good afternoon sir, it's {tt}")
    else:
        speak(f"Good evening sir, it's {tt}")

# Function to check battery status
def battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Sir, our system has {percentage} percent battery")
    
    if percentage >= 75:
        speak("We have sufficient power to do our tasks")
    elif 40 <= percentage <= 75:
        speak("We have enough power to continue our work")
    elif 15 <= percentage <= 40:
        speak("We don't have enough power to work, please connect to charging")
    elif percentage <= 15:
        speak("Battery is low, please connect to charging. The system will shut down soon.")
    elif percentage <= 5:
        speak("Battery is critically low.")

# Function to check birthdays
def birthday():
    df = read_csv("birthday.csv", sep=',')
    df = DataFrame(df, columns=['name', 'month', 'date'])
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    blist = []

    for i in range(len(df)):
        try:
            if month == df['month'][i] and day == df['date'][i]:
                blist.append(df['name'][i])
        except IndexError:
            break
        
    for name in blist:
        if name == 'Your Name':
            speak("Happy birthday sir")
        else:
            speak(f"Today is the birthday of {name}")

# Function to check internet connection
def conn():
    speak("Checking internet connection...")
    
    def test_connection():
        try:
            socket.create_connection(('Google.com', 80))
            return True
        except OSError:
            return False

    if not test_connection():
        speak("You are not connected to the internet. Please connect for online information.")
    else:
        speak("You are connected to the internet.")
        temp()

# Function to fetch temperature
def temp():
    search = "temperature of my location"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature1 = data.find("div", class_="BNeawe").text
    temperature_string = temperature1
    temperature = re.search(r'\d+', temperature_string).group()
    temperature = int(temperature)
    speak(f"The weather outside is {temperature1}")
    
    if temperature >= 30:
        speak("It's too hot outside")
    elif temperature >= 20:
        speak("Temperature is normal outside")
    elif temperature >= 10:
        speak("Temperature is pleasant outside")
    elif temperature <= 10:
        speak("Temperature is cold outside")
    elif temperature <= 5:
        speak("Temperature is very cold outside")


# Main function for task execution
def task_execution():
    speak("Welcome back sir.")
    speak("All systems and settings will be prepared in a few moments.")
    speak("Feel free to grab a cup of coffee.")
    speak("Loading intro...")
    speak("Now, let me introduce myself. I am Alpha, your personal artificial intelligence software, always ready for you.")
    speak("I am here to assist you in a variety of tasks.")
    speak("Initializing Alpha...")
    speak("Initial checks completed. Installing and checking all drives. Calibrating data. Scanning files...")
    speak("Security checks are looking good.")
    conn()
    speak("Systems and settings are running properly. Now you are ready to execute your tasks.")
    wish()
    battery()
    birthday()
    speak("Let's do some great tasks, sir.")

if __name__ == "__main__":
    task_execution()
