import streamlit as st
import numpy as np
import pickle
import base64

# Load model
model = pickle.load(open("wildfire_model.pkl","rb"))



def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

set_background("background.jpg")

model = pickle.load(open("wildfire_model.pkl","rb"))

st.title("🔥 Forest Wildfire Burned Area Prediction")

X = st.number_input("X Coordinate")
Y = st.number_input("Y Coordinate")
FFMC = st.number_input("FFMC")
DMC = st.number_input("DMC")
DC = st.number_input("DC")
ISI = st.number_input("ISI")
temp = st.number_input("Temperature")
RH = st.number_input("Relative Humidity")
wind = st.number_input("Wind Speed")
rain = st.number_input("Rainfall")

if st.button("Predict"):

    input_data = np.array([[X,Y,FFMC,DMC,DC,ISI,temp,RH,wind,rain]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Burned Area: {prediction[0]:.2f}")