import streamlit as st
import requests

st.title("Monitoring")

if st.button("Dapatkan Data Acak"):
    response = requests.get("https://legal-poets-float.loca.lt/random-data")
    data = response.json()
    st.write(f"Data Acak: {data['data']}")
