import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("wildfire_model.pkl","rb"))

st.title("🔥 Forest Wildfire Burned Area Prediction")

# Sidebar Image
st.sidebar.image("background.jpg", caption="Wildfire", use_container_width=True)

st.sidebar.header("Enter Fire Parameters")

col1, col2 = st.columns([3,1])

with col2:
    st.image("background.jpg", width=200)

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
