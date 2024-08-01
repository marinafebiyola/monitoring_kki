import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    response = requests.get("https://tangy-pears-cover.loca.lt/random-data")
    data = response.json()
    data_placeholder.write(f"Data Acak: {data['data']}")
    time.sleep(5)  # Adjust the sleep time as needed to control the update frequency
