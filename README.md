# Streamlit Weather App

This is a simple Streamlit application that retrieves current weather data using OpenWeather.

## Features

- Enter a city in the Streamlit app
- Retrieve current weather data from OpenWeather
- Display temperature in Celsius
- Display humidity
- Display current weather conditions

## Installation

1. Clone the repository.

2. Create a virtual environment:

    python -m venv .venv

3. Activate the virtual environment.

4. Install the required packages:

    pip install streamlit requests python-dotenv

## API Key

Create a `.env` file in the project directory.

Add your OpenWeather API key.

## Run the App

Run the following command:

    python -m streamlit run app.py

Open the URL in your browser and enter a city to view its current weather.