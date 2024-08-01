import streamlit as st
import requests
import time

st.title("Monitoring system")

data_placeholder = st.empty()

while True:
    try:
        response = requests.get("https://late-berries-cough.loca.lt/random-data", timeout=5)  # Tambahkan timeout
        response.raise_for_status()  # Periksa jika request berhasil
        data = response.json()  # Coba parse response sebagai JSON
        data_placeholder.write(f"Data Acak: {data['data']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request gagal: {e}")
        time.sleep(10)  # Tunggu lebih lama sebelum mencoba lagi
        continue  # Lewati parsing JSON jika terjadi error
    except requests.exceptions.JSONDecodeError:
        st.error("Gagal memparse response JSON")
    except KeyError as e:
        st.error(f"KeyError: {e} pada response JSON")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
        time.sleep(10)  # Tunggu sebelum mencoba lagi
        continue
    time.sleep(1)  # Sesuaikan waktu delay sesuai kebutuhan
