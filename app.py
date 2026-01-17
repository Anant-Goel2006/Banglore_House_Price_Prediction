import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('house_model.pkl')

st.title("🏡 House Price Predictor")
st.write("Enter the details of the house to get an estimated price.")

# Create input fields based on the features in your notebook
# Example: If your model uses 'SquareFeet', 'Bedrooms', and 'Bathrooms'
sqft = st.number_input("Square Footage", min_value=500, max_value=10000, value=1500)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 5, 2)

# Create a prediction button
if st.button("Predict Price"):
    # Arrange inputs into a dataframe or array matching your model's training format
    input_data = pd.DataFrame([[sqft, bedrooms, bathrooms]], 
                              columns=['SquareFeet', 'Bedrooms', 'Bathrooms'])
    
    prediction = model.predict(input_data)
    
    st.success(f"The estimated price for this house is ${prediction[0]:,.2f}")
