import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Machine Learning Model",
    page_icon="🤖",
    layout="centered"  # Change layout to centered for smaller width so the image fits the screen properly
)

st.markdown("# Train and Predict with Linear Regression")
st.markdown("""
This page trains a Linear Regression model and dynamically updates predictions and visualizations based on user input.
""")

# Load dataset from session state
if "combined_df" in st.session_state:
    df = st.session_state.combined_df.copy()

    # Select features and target
    feature_names = ["Body Mass Index", "Blood Glucose after fasting", "Blood Insulin Levels", "Gender"]
    X = df[feature_names]
    y = df["Age"]

    # Handle missing values
    X = X.fillna(X.mean())  # Impute missing values with column means
    y = y.fillna(y.mean())  # Impute missing values with column mean

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Sidebar inputs
    st.sidebar.markdown("# Make Predictions")
    bmi = st.sidebar.slider("Body Mass Index", float(X["Body Mass Index"].min()), float(X["Body Mass Index"].max()))
    glucose = st.sidebar.slider("Blood Glucose after fasting", float(X["Blood Glucose after fasting"].min()), float(X["Blood Glucose after fasting"].max()))
    insulin = st.sidebar.slider("Blood Insulin Levels", float(X["Blood Insulin Levels"].min()), float(X["Blood Insulin Levels"].max()))
    gender = st.sidebar.radio("Gender", [1, 2])  # 1: Female, 2: Male

    # Prepare input for prediction
    input_data = pd.DataFrame([[bmi, glucose, insulin, gender]], columns=feature_names)  # Add feature names
    predicted_age = model.predict(input_data)[0]

    st.markdown(f"### Predicted Age: {predicted_age:.2f} years")

    # Visualization
    st.markdown("## Visualization")
    fig, ax = plt.subplots()

    # Scatter plot for test set predictions (add transparency)
    ax.scatter(
        X_test["Body Mass Index"], y_test,
        color="blue", alpha=0.5, label="Actual (Test Set)"
    )
    ax.scatter(
        X_test["Body Mass Index"], model.predict(X_test),
        color="red", alpha=0.5, label="Predicted (Test Set)"
    )

    # Add slider-based prediction as a prominent marker
    ax.scatter(
        [bmi], [predicted_age],
        color="yellow", s=150, label="Your Prediction", marker="X", edgecolors="black"
    )

    # Plot labels and title
    ax.set_title("Actual vs. Predicted Age")
    ax.set_xlabel("Body Mass Index")
    ax.set_ylabel("Age")

    # Place legend outside at the bottom
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=3,  # Number of columns in the legend
        frameon=False
    )

    st.pyplot(fig)

else:
    st.error("Dataset not found. Please navigate back to the data handling page to process the dataset.")
