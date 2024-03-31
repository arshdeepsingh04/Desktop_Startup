# Desktop Startup Assistant for Daily Tasks

## Overview
Desktop Startup Assistant is a Python script designed to act as a personal assistant for daily tasks. It utilizes various libraries to provide functionalities such as time-based greetings, battery status checks, birthday reminders, internet connection verification, and weather updates. Enhanced with text-to-speech capabilities using pyttsx3, the assistant delivers spoken updates on essential daily information.

## Features
- Time-Based Greetings: The assistant greets the user based on the time of day, providing a personalized touch to the interaction.
- Battery Status Check: It monitors the system's battery status and notifies the user about the current battery level, ensuring uninterrupted usage.
- Birthday Reminders: Utilizing a CSV file containing birthday data, the assistant reminds the user of any birthdays occurring on the current day.
- Internet Connection Check**: Verifies the availability of internet connectivity and alerts the user if a connection is not detected.
- Weather Updates: Using web scraping techniques, the assistant fetches real-time weather information based on the user's location, providing valuable insights for planning outdoor activities.
- Task Execution: After initializing and performing necessary checks, the assistant prompts the user to proceed with executing tasks, ensuring a seamless user experience.

## Installation
To run the script, ensure you have Python installed on your system along with the required libraries:
- pyttsx3
- psutil
- requests
- bs4 (Beautiful Soup)
- pandas

You can install these libraries using pip:
```
pip install pyttsx3 psutil requests pandas
pip install beautifulsoup4
```

## Usage
1. Clone the repository to your local machine.
2. Ensure you have a CSV file named `birthday.csv` containing birthday data in the format: `name, month, date`.
3. Execute the Python script `startup.pyw`.
4. Follow the prompts and interact with the assistant for various tasks.

## Example
```
python startup.pyw
```

## Notes
- Customize the code according to your preferences and system configurations for optimal performance.
- Consider extending the functionality by adding features such as email notifications or task scheduling to further enhance user productivity.
- Contributions and feedback are welcome to tailor the assistant to meet diverse user needs effectively.
