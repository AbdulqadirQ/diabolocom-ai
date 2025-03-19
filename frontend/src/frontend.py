# EXPLANATION: streamlit is a very easy to use and quick way to acheive a front-end interface
#              since the main audience for this app is potentially a non-technical user, an
#              easy interface would have been good to have. It works when run natively but not
#              within a container
import os
import requests
import streamlit as st

API_BASE_URL = os.environ["API_BASE_URL"]

st.set_page_config(page_title="🦜 Diabolocom AI Transcription")
st.title('Diabolocom AI Transcription')
# EXPLANATION: loads a file uploaded by the user
file = st.file_uploader("Upload a recording to transcribe...")

# EXPLANATION: upon pressing the button, a request is sent to the API for transcription
if st.button("Transcribe!"):
    response = requests.post(url = f"http://{API_BASE_URL}/upload_call/", files={"file": file})
    st.divider()
    container = st.container(border=True)
    # The transcription is displayed to the user in an easy to read format within the same page
    container.write(response.json()["transcription"])
