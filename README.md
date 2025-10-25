# 🌤️ Weather App – Python Project

A beginner-friendly Python app that fetches real-time weather data for any city using the OpenWeatherMap API.

## 🔧 Technologies Used

- Python 3
- Requests
- python-dotenv
- OpenWeatherMap API

## 🚀 How to Run This Project

1. Clone this repository:
   ```bash
   git clone https://github.com/siripodichetti/weather-app.git
   cd weather-app


2. Install required packages:
pip install -r requirements.txt

*(Or manually install: `pip install requests python-dotenv`)*

3. Create a `.env` file in the root folder and add your API key:
API_KEY=your_api_key_here


4. Run the script:
python weather.py


## ✅ Features

- Real-time weather data by city
- Temperature and description display
- API key secured using `.env`
- Graceful error handling for bad input or failed requests

## 📌 Future Improvements

- Add humidity, wind speed, sunrise/sunset
- Support multiple cities
- Add a GUI (Tkinter or Flask web app)
- Handle invalid inputs more gracefully

## 📸 Example Output

Enter city name: Delhi

Weather in Delhi: 34°C, Scattered clouds



This is a beginner project for learning and sharing. Feel free to fork it, open issues, or suggest improvements!

