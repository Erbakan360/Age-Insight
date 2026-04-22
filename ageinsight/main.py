import streamlit as st
import pandas as pd

# Set page configuration to enable wide layout
st.set_page_config(
    page_title="Age Insight",  # Title of the web app
    page_icon="📊",           # Emoji or image as the app icon
    layout="wide"             # Use full-width layout
)

st.markdown("""
# Age Insight

This app provides insights into health and age prediction based on a dataset containing variables such as age, gender, BMI, glucose levels, and insulin levels.

You can explore the data and get insights such as:
- *Health trends* across different age groups.
- *The relationship* between health parameters and age prediction.
- *Predictions for age groups* based on user inputs.

## Dataset Overview

The dataset contains the following columns:
- **ID**: Unique identifier for each individual.
- **Age_group**: Categorized age group (e.g., Adult).
- **Age**: Exact age of the individual.
- **Gender**: Encoded gender (1 = Female, 2 = Male).
- **PAQ605**: Indicator of physical activity levels.
- **Body Mass Index**: BMI of the individual.
- **Blood Glucose after fasting**: Fasting glucose levels in mg/dL.
- **Diabetic or not**: Indicates diabetes status (1 = Diabetic, 2 = Non-diabetic).
- **Respondent's Oral**: Measure related to oral health.
- **Blood Insulin Levels**: Insulin levels in μIU/mL.
""")

# Placeholder for data loading section
st.markdown("## Data Acquisition")
st.write("The dataset has been loaded successfully.")

# Load the CSV file into a DataFrame
file_path = 'data/Age Prediction.csv'
try:
    df = pd.read_csv(file_path)
    st.session_state.original_df = df
except FileNotFoundError:
    st.error("Dataset not found. Please ensure the dataset file is in the correct directory.")