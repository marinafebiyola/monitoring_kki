import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    try:
        response = requests.get("https://tangy-pears-cover.loca.lt/random-data")
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Attempt to parse the response as JSON
        data_placeholder.write(f"Data Acak: {data['data']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
    except requests.exceptions.JSONDecodeError:
        st.error("Failed to parse JSON response")
    time.sleep(5)  # Adjust the sleep time as needed to control the update frequency

