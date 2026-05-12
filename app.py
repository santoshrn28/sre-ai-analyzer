import streamlit as st
import requests

st.title("SRE Log Analyzer")

file = st.file_uploader("Upload support bundle")

if file:
    res = requests.post(
        "http://localhost:8000/analyze/",
        files={"file": file}
    )

    st.write(res.json())
