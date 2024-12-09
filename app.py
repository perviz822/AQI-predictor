import streamlit as st
from home import display_aqi_prediction_page
from about import about_page
st.set_page_config(layout="wide")
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to",["Home","About"])



if page =="Home":
    display_aqi_prediction_page()
elif page=="About": 
    about_page()  