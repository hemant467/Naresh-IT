import streamlit as st
import numpy as np
import joblib
import sklearn

# --- PAGE CONFIG ---
st.set_page_config(page_title="California House Price Predictor", page_icon="🏠", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            color: #333333;
        }
        /* Title Card */
        .title-card {
            background-color: #2E86C1;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        /* Subtitle */
        .sub-title {
            color: #117A65;
            font-size: 18px;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Predict Button */
        div.stButton > button:first-child {
            background-color: #FF5733;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            height: 50px;
            width: 150px;
        }
        div.stButton > button:hover {
            background-color: #C70039;
            color: white;
        }
        /* Input Panel */
        .input-panel {
            background-color: #E8F6F3;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE CARD ---
st.markdown("<div class='title-card'>California House Price Predictor 🏠</div>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Enter the details below to predict the median house value in California</p>", unsafe_allow_html=True)

# --- INPUT PANEL ---
with st.container():
    st.markdown("<div class='input-panel'>", unsafe_allow_html=True)

    MedInc = st.number_input('Median Income (MedInc)', min_value=0.0, format="%.2f")
    HouseAge = st.number_input('House Age', min_value=0.0, format="%.2f")
    AveRooms = st.number_input('Average Rooms (AveRooms)', min_value=0.0, format="%.2f")
    Population = st.number_input('Population', min_value=0.0, format="%.2f")
    AveOccup = st.number_input('Average Occupancy (AveOccup)', min_value=0.0, format="%.2f")
    Latitude = st.number_input('Latitude', format="%.4f")

    st.markdown("</div>", unsafe_allow_html=True)

# --- LOAD MODEL ---
location = 'california_model.joblib'
saved_model = joblib.load(location)

# --- PREDICT BUTTON ---
if st.button('Predict'):
    Input = [MedInc, HouseAge, AveRooms, Population, AveOccup, Latitude]
    op = saved_model['model'].predict([Input])
    st.success(f"🏡 Estimated Median House Value: **${op[0]:,.2f}**")
