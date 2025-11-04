# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Weather App (No API Key)", layout="centered")

st.title("🌤️ Free Weather App")
st.markdown("Using [wttr.in](https://wttr.in)")

city = st.text_input("Enter city name", "Seoul")

if st.button("Get Weather"):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()

        current = data["current_condition"][0]
        weather_desc = current["weatherDesc"][0]["value"]
        temp_c = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]

        st.subheader(f"Weather in {city}")
        st.metric("Temperature", f"{temp_c} °C")
        st.metric("Feels Like", f"{feels_like} °C")
        st.metric("Humidity", f"{humidity}%")
        st.metric("Wind", f"{wind} km/h")
        st.markdown(f"**Condition:** {weather_desc}")

        st.image(f"https://wttr.in/{city}.png", caption="Forecast (from wttr.in)")

    except Exception as e:
        st.error(f"Failed to fetch weather: {e}")
