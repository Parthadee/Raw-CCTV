import streamlit as st
import requests

st.title(
    "Store Intelligence"
)

data = requests.get(
    "http://localhost:8000/stores/STORE_BLR_002/metrics"
).json()

st.metric(
    "Conversion Rate",
    data["conversion_rate"]
)