import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Feature Engineering",
    page_icon="🔧",
    layout="wide"
)

st.markdown("# Feature Engineering")
st.markdown("""
This page enables the selection and transformation of feature variables to prepare the dataset for machine learning.
""")

# Load dataset from session state
if "original_df" in st.session_state:
    df = st.session_state.original_df.copy()

    # Display original dataset
    st.markdown("## Original Dataset")
    st.write(df.head())

    # Drop unnecessary columns
    st.markdown("## Column Selection")
    st.markdown("Select the columns you want to retain for further analysis:")
    columns_to_keep = st.multiselect("Columns to keep:", options=df.columns, default=df.columns.tolist())
    
    if columns_to_keep:
        df = df[columns_to_keep]
        st.markdown("### Updated Dataset")
        st.write(df.head())
    else:
        st.warning("Please select at least one column to retain.")

    # Transform features
    st.markdown("## Feature Transformation")
    st.markdown("""
    Transform columns to improve their interpretability or prepare them for modeling.
    Below are some common transformations:
    - Log transformation for skewed data.
    - Scaling for numeric columns.
    """)

    # Example: Log Transformation
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_columns:
        st.markdown("### Log Transformation")
        columns_to_log = st.multiselect(
            "Select numeric columns to apply log transformation:",
            options=numeric_columns,
            default=[]
        )
        for col in columns_to_log:
            df[col] = np.log1p(df[col])
        st.write("Log-transformed dataset:")
        st.write(df.head())
    else:
        st.warning("No numeric columns available for transformation.")

    # Scaling (Normalization)
    st.markdown("### Scaling (Normalization)")
    scaling_columns = st.multiselect(
        "Select numeric columns to scale (min-max normalization):",
        options=numeric_columns,
        default=[]
    )
    if scaling_columns:
        for col in scaling_columns:
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        st.write("Scaled dataset:")
        st.write(df.head())

    # Update session state
    st.session_state.feature_engineered_df = df

else:
    st.error("Dataset not found. Please navigate back to the data loading page.")
