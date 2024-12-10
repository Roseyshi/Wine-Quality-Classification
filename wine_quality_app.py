import streamlit as st
from joblib import load

# Load the model
loaded_rf = load('best_random_forest_model.joblib')

# Use 'rf' for predictions in your Streamlit app
st.title("Wine Quality Classification App")

# Input fields
feature1 = st.number_input("volatile acidity")
feature2 = st.number_input("total sulfur dioxide")
feature3 = st.number_input("free sulfur dioxide")
feature4 = st.number_input("citric acid")
feature5 = st.number_input("alcohol")
feature6 = st.number_input("chlorides")
feature7 = st.number_input("fixed acidity")
feature8 = st.number_input("pH")
feature9 = st.number_input("density")
feature10 = st.number_input("residual sugar")
feature11 = st.number_input("sulphates")

if st.button("Predict"):
    prediction = rf.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                              feature9, feature10, feature11]])
    st.write(f"Predicted Class: {data.target_names[prediction[0]]}")
