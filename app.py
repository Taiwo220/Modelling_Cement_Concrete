import streamlit as st
import pickle

# Load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

# Set the title of the app
st.title("Concrete Strength Prediction")

# Input fields for user data
Cement = st.number_input("Cement (kg)", min_value=0.0)
Blast_Furnace_Slag = st.number_input("Blast Furnace Slag (kg)", min_value=0.0)
Fly_Ash = st.number_input("Fly Ash (kg)", min_value=0.0)
Water = st.number_input("Water (kg)", min_value=0.0)
Superplasticizer = st.number_input("Superplasticizer (kg)", min_value=0.0)
Coarse_Aggregate = st.number_input("Coarse Aggregate (kg)", min_value=0.0)
Fine_Aggregate = st.number_input("Fine Aggregate (kg)", min_value=0.0)
Age_day = st.number_input("Age (days)", min_value=0)

# Button to trigger prediction
if st.button("Predict"):
    try:
        # Prepare input data for prediction
        input_data = [[Cement, Blast_Furnace_Slag, Fly_Ash, Water,
                       Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age_day]]
        
        # Make a prediction using the model
        result = model.predict(input_data)[0]

        # Display the prediction result
        st.success(f"Predicted Concrete Strength: {result:.2f} MPa")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
