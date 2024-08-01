import streamlit as st
import requests

st.title("Monitoring")

# URL dari local tunnel yang mengarah ke backend Flask Anda
backend_url = "https://plenty-bobcats-travel.loca.lt/api/data"

if st.button("Dapatkan Data Acak"):
    try:
        # Mengirim permintaan GET ke backend Flask
        response = requests.get(backend_url)
        # Memeriksa apakah respons berhasil
        if response.status_code == 200:
            data = response.json()
            st.write(f"Data Acak: {data['value']}")
        else:
            st.write(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write(f"Permintaan gagal: {e}")
