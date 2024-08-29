
Weather App
Overview
The Weather App allows users to get the current weather of any city and provides additional features like a 5-day weather forecast, weather information based on the user's location, and a visually appealing interface with weather icons. The app is built using Python and Flask, and it fetches real-time weather data using the OpenWeatherMap API.

Features
Search by City: Enter any city to get the current weather conditions.
Current Weather Details: Display temperature, weather description, humidity, wind speed, and more.
5-Day Forecast: Provides a 5-day weather forecast for the selected city.
Location-based Weather: Fetch weather data based on the user's current location.
Weather Icons: Uses weather icons to visually represent the weather conditions.
Info Section: Contains the developer’s name (Venkata Lakshmi Lahari Appala) and an info button to view a description of PM Accelerator, linking to the LinkedIn page.
Prerequisites
Python 3.x
Flask
requests library for handling API requests
geocoder for obtaining the user's location
Installing Required Libraries
To install the required Python libraries, run the following command:

bash
Copy code
pip install flask requests geocoder
How to Run the Project
Clone the repository:

bash
Copy code
git clone https://github.com/lakshmilahari25/Weather.git
Navigate to the project directory:

bash
Copy code
cd Weather
Set up your OpenWeatherMap API key:

Sign up on OpenWeatherMap to get an API key.
Open app.py and replace your_api_key_here with your actual OpenWeatherMap API key.
Run the Flask application:

bash
Copy code
python app.py
Open a browser and navigate to http://127.0.0.1:5000/.

Enter the city name in the search bar to get the current weather, or click the Location Weather button to get weather info for your current location.

Folder Structure
php
Copy code
Weather/
│
├── app.py               # Main Flask app
├── static/
│   ├── css/
│   └── images/          # Weather icons and other static files
├── templates/
│   └── index.html       # HTML file for displaying weather information
└── README.md            # Project README file
