import streamlit as st
import pandas as pd

# Set page configuration to align with the app's theme
st.set_page_config(
    page_title="Numericisation of Data",
    page_icon="🔄",
    layout="wide"
)

st.markdown("# Numericisation of Data")
st.markdown("""
This page allows you to transform the dataset by replacing specific values in the `Age_group` column:
- Replace "Adult" with `0`
- Replace "Seniors" with `1`

Both the original and transformed datasets are displayed in full.
""")

# Load dataset from session state
if "original_df" in st.session_state:
    # Original dataset
    df_original = st.session_state.original_df.copy()

    st.markdown("## Original Data")
    st.write(df_original)

    # Clean and transform the data
    df_transformed = df_original.copy()
    if "Age_group" in df_transformed.columns:
        # Clean the data (remove leading/trailing spaces and standardize case)
        df_transformed["Age_group"] = df_transformed["Age_group"].str.strip().str.title()
        
        # Replace values
        df_transformed["Age_group"] = df_transformed["Age_group"].replace({"Adult": 0, "Senior": 1})

        st.markdown("## Transformed Data")
        st.write(df_transformed)

    else:
        st.error("The column 'Age_group' does not exist in the dataset.")

else:
    st.error("Dataset not found. Please navigate back to the main page to load the dataset.")
