import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# App title
st.title("Weather App!")

# Ask the user for a city
city = st.text_input("Weather in which city are you interested in?")

# Run when the user clicks the button
if st.button("Get Weather"):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    st.write("Status code:", response.status_code)
    st.write("API response:", data)

    # Check if the API request was successful
    if response.status_code == 200:

        # Extract weather information
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Display weather information
        st.subheader(f"Weather in {data['name']}")
        st.write(f"Temperature: {temperature}C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Conditions: {description}")

    else:
        st.error("City not found. Please try again.")