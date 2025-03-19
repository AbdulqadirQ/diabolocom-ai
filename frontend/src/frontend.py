import os
import requests
import streamlit as st

API_BASE_URL = os.environ["API_BASE_URL"]

st.set_page_config(page_title="🦜 Diabolocom AI Transcription")
st.title('Diabolocom AI Transcription')
file = st.file_uploader("Upload a recording to transcribe...")

if st.button("Transcribe!"):
    response = requests.post(url = f"http://{API_BASE_URL}/upload_call/", files={"file": file})
    st.divider()
    container = st.container(border=True)
    container.write(response.json()["transcription"])
