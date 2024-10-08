import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('savedmodel.sav', 'rb'))

# Set the title of the app
st.title("Concrete Strength Prediction App")

# Sidebar for navigation
menu = ["Single Prediction", "Predict with CSV"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Single Prediction":
    # Single Prediction Page
    st.subheader("Input values for concrete strength prediction")

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

elif choice == "Predict with CSV":
    # CSV Upload and Prediction Page
    st.subheader("Upload your CSV file for batch prediction")

    # Display required columns
    required_columns = ['Cement', 'Blast Furnace Slag', 'Fly Ash', 'Water', 
                        'Superplasticizer', 'Coarse Aggregate', 'Fine Aggregate', 'Age (day)']
    
    st.write(f"Your CSV file must contain the following columns: {', '.join(required_columns)}")

    # File uploader for CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded data:")
        st.write(data)

        # Check if the required columns are present
        if all(column in data.columns for column in required_columns):
            # Make predictions
            predictions = model.predict(data[required_columns])

            # Add predictions to the dataframe
            data['Predicted Strength'] = predictions
            st.write("Predictions:")
            st.write(data)

            # Provide download button for the predictions
            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")

        else:
            st.error(f"CSV file must contain the following columns: {required_columns}")
