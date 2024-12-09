import streamlit as st

def about_page():
 
 st.title("About page")
 st.header("Understanding AQI")
 st.subheader("Why It Matters")
 st.write("""The Air Quality Index (AQI) is like a health checkup for the air you breathe. It’s a number that tells you how clean or polluted the air is and how it might affect you.
If the AQI is "Good," the air is fresh and safe. If it’s "Hazardous," it’s best to stay indoors because breathing could be harmful. This number is based on pollutants like tiny particles (PM2.5) and gases such as ozone and carbon monoxide.
Think of AQI as your guide to decide whether it’s safe to enjoy outdoor activities or take extra care for your health. Simple, helpful, and important! 🌿""")
 st.write("""
    <b>Particulate Matter (PM2.5 and PM10)</b><br/>
    These are tiny particles floating in the air, often too small to see. PM2.5 refers to fine particles, like smoke or vehicle emissions, that can penetrate deep into your lungs. PM10 includes larger particles, like dust and pollen, which can irritate your airways. These pollutants often come from factories, construction sites, and wildfires.<br/><br/>
    <b>Ground-Level Ozone</b><br/>
    Ozone at ground level isn’t the same as the protective ozone layer in the sky. It forms when sunlight reacts with pollutants like car exhaust and industrial emissions. While it’s invisible, it can cause breathing difficulties and throat irritation, especially on hot, sunny days.<br/><br/>
    <b>Nitrogen Dioxide (NO2)</b><br/>
    This gas mainly comes from burning fuel, such as in vehicles and power plants. It can irritate your respiratory system and contribute to smog. High levels are common in urban areas with heavy traffic.<br/><br/>
    <b>Sulfur Dioxide (SO2)</b><br/>
    Emitted by burning fossil fuels, particularly coal and oil, sulfur dioxide has a sharp, choking smell. It can aggravate asthma and combine with water in the air to form acid rain.<br/><br/>
    <b>Carbon Monoxide (CO)</b><br/>
    Carbon monoxide is a colorless, odorless gas produced by incomplete combustion, like in car engines or poorly ventilated stoves. It reduces oxygen in the blood, making it dangerous at high levels, especially indoors.
""", unsafe_allow_html=True)
