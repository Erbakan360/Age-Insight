import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Model Comparison",
    page_icon="📊",
    layout="wide"
)

st.markdown("# Compare Regression Models")
st.markdown("""
This page compares Linear Regression and Random Forest Regression to select the best model for age prediction.
""")

# Load dataset from session state
if "combined_df" in st.session_state:
    df = st.session_state.combined_df.copy()

    # Select features and target
    feature_names = ["Body Mass Index", "Blood Glucose after fasting", "Blood Insulin Levels", "Gender"]
    X = df[feature_names]
    y = df["Age"]

    # Handle missing values
    X = X.fillna(X.mean())
    y = y.fillna(y.mean())

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_predictions = lr_model.predict(X_test)

    # Train Random Forest Regression model
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)

    # Calculate performance metrics
    lr_mse = mean_squared_error(y_test, lr_predictions)
    lr_r2 = r2_score(y_test, lr_predictions)

    rf_mse = mean_squared_error(y_test, rf_predictions)
    rf_r2 = r2_score(y_test, rf_predictions)

    # Display metrics
    st.markdown("## Model Performance")
    metrics = pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest Regression"],
        "Mean Squared Error": [lr_mse, rf_mse],
        "R-squared": [lr_r2, rf_r2]
    })
    st.write(metrics)

    # Determine the better model
    better_model = "Linear Regression" if lr_r2 > rf_r2 else "Random Forest Regression"

    st.markdown(f"### Selected Model: {better_model}")

    # Create a separate page for the selected model
    st.markdown("## Details of the Selected Model")
    if better_model == "Linear Regression":
        st.markdown("### Linear Regression")
        st.write(f"MSE: {lr_mse:.2f}, R-squared: {lr_r2:.2f}")
    else:
        st.markdown("### Random Forest Regression")
        st.write(f"MSE: {rf_mse:.2f}, R-squared: {rf_r2:.2f}")

else:
    st.error("Dataset not found. Please navigate back to the data handling page to process the dataset.")
