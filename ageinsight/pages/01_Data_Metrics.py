import streamlit as st
import matplotlib.pyplot as plt

# Configuring the Streamlit page layout and metadata
st.set_page_config(
    page_title="AgeInsight Data Metrics",
    page_icon="📈",
    layout="wide"
)

# Page Header
st.markdown("# Data Metrics")
st.markdown("""
This page provides detailed metrics and visualizations of the dataset 
to help analyze the distribution and relationships between variables.
""")

# Function to display dataset overview
def display_dataset_overview(dataframe):
    """Display the first few rows of the dataset and summary statistics."""
    st.markdown("## Dataset Overview")
    st.write(dataframe.head())
    st.markdown("## Summary Statistics")
    st.write(dataframe.describe())

# Function to display data types
def display_data_types(dataframe):
    """Display the data types of each column in the dataset."""
    st.markdown("## Data Types")
    data_types = dataframe.dtypes.to_frame().transpose()  # Transpose for better readability
    st.dataframe(data_types)

# Function to preprocess specific columns
def preprocess_columns(dataframe):
    """Preprocess specific columns, e.g., 'Age Group', if they exist."""
    if "Age Group" in dataframe.columns:
        dataframe["Age Group"] = dataframe["Age Group"].replace({"Adult": 0, "Senior": 1}).fillna(-1).astype(float)
    return dataframe

# Function to generate and display correlation heatmap
def display_correlation_heatmap(dataframe):
    """Generate and display the correlation heatmap for numeric columns."""
    st.markdown("## Feature Correlations")
    numeric_df = dataframe.select_dtypes(include=["number"])  # Select numeric columns
    corr_matrix = numeric_df.corr()  # Compute correlations
    st.write(corr_matrix)

# Function to create and display visualizations
def create_visualizations(dataframe):
    """Generate and display visualizations in a 2 x 2 grid."""
    col1, col2 = st.columns(2)

    with col1:
        # Age distribution
        st.markdown("### Distribution of Age")
        plot_histogram(dataframe, "Age", "Age Distribution", "Age", "Frequency")

        # Blood Glucose distribution
        st.markdown("### Distribution of Blood Glucose Levels")
        plot_histogram(dataframe, "Blood Glucose after fasting", "Glucose Levels Distribution", "Glucose Level", "Frequency", color='green')

    with col2:
        # BMI distribution
        st.markdown("### Distribution of BMI")
        plot_histogram(dataframe, "Body Mass Index", "BMI Distribution", "BMI", "Frequency", color='orange')

        # Gender distribution
        st.markdown("### Gender Distribution")
        plot_bar_chart(dataframe["Gender"].value_counts(), "Gender Distribution", "Gender", "Count")

# Helper function to plot histograms
def plot_histogram(dataframe, column, title, xlabel, ylabel, color='skyblue'):
    """Helper function to create a histogram."""
    fig, ax = plt.subplots()
    ax.hist(dataframe[column], bins=20, color=color, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Helper function to plot bar charts
def plot_bar_chart(data, title, xlabel, ylabel):
    """Helper function to create a bar chart."""
    fig, ax = plt.subplots()
    ax.bar(data.index, data, color=['lightblue', 'blue'])
    ax.set_title(title)
    ax.set_xticks(data.index)
    ax.set_xticklabels(data.index)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Main application logic
if "original_df" in st.session_state:
    df = st.session_state.original_df

    # Display dataset overview and data types
    display_dataset_overview(df)
    display_data_types(df)

    # Preprocess dataset and display correlation heatmap
    df = preprocess_columns(df)
    display_correlation_heatmap(df)

    # Generate visualizations
    create_visualizations(df)
else:
    st.error("Dataset not found. Please navigate back to the main page to load the dataset.")
