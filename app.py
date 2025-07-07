import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("house_price_prediction.joblib")

st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")

st.title("🏠 Bangalore House Price Prediction")
st.markdown("Predict the price of a house based on its features.")

# User inputs
location = st.text_input("📍 Location", "Electronic City Phase II")
total_sqft = st.number_input("📐 Total Square Feet", min_value=100.0, max_value=10000.0, step=10.0, value=1200.0)
bath = st.number_input("🛁 Number of Bathrooms", min_value=1.0, max_value=10.0, step=1.0, value=2.0)
balcony = st.number_input("🌅 Number of Balconies", min_value=0.0, max_value=5.0, step=1.0, value=1.0)
bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=1, max_value=10, step=1, value=2)

# Predict button
if st.button("🔍 Predict Price"):
    try:
        input_df = pd.DataFrame([[location, total_sqft, bath, balcony, bedrooms]],
                                columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Price: ₹ {round(prediction, 2)} Lakhs")
    except Exception as e:
        st.error(f"❌ Error: {e}")
