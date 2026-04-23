import streamlit as st
import pickle
import numpy as np

# 1. Load the model
with open('heart_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("❤️ Heart Disease Predictor")

# 2. Create 9 input fields (Adjust labels/ranges to match your specific dataset)
col1, col2, col3 = st.columns(3) # This makes the UI look cleaner in columns

with col1:
    age = st.number_input("Age", 1, 100, 25)
    sex = st.selectbox("Sex (1=M, 0=F)", [1, 0])
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])

with col2:
    trestbps = st.number_input("Resting BP", 50, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [0, 1])

with col3:
    restecg = st.selectbox("Resting ECG (0-2)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate", 50, 220, 150)
    exang = st.selectbox("Exercise Angina (1=Yes, 0=No)", [0, 1])

# 3. Prediction Button
if st.button("Predict"):
    # CRITICAL: The order here must match the order of your CSV columns exactly!
    input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang]
    
    # Reshape for the model
    features = np.array([input_data])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("Warning: High risk of heart disease.")
    else:
        st.success("Result: Low risk detected.")