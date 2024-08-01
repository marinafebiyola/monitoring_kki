import streamlit as st
import requests

st.title("Monitoring")

if st.button("Dapatkan Data Acak"):
    try:
        # Mengirim permintaan GET ke backend Flask
        response = requests.get("https://plenty-bobcats-travel.loca.lt/data")
        # Memeriksa apakah respons berhasil
        if response.status_code == 200:
            data = response.json()
            st.write(f"Data Acak: {data['value']}")
        else:
            st.write(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write(f"Permintaan gagal: {e}")
