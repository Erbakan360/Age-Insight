import streamlit as st

# Ensure the dataset is already loaded in the session state
if "original_df" not in st.session_state:
    st.error("Dataset not loaded. Please navigate to the main page to load the dataset.")
else:
    # Load the dataset from session state
    df = st.session_state.original_df

    # Chatbot response logic
    def chatbot_response(user_input, df):
        user_input = user_input.lower()

        if "columns" in user_input:
            return f"The dataset contains the following columns:\n{', '.join(df.columns)}"

        elif "summary" in user_input:
            return f"Here is the summary of the dataset:\n\n{df.describe(include='all').to_string()}"

        elif "missing values" in user_input:
            missing_values = df.isnull().sum()
            return f"Missing values in each column:\n{missing_values.to_string()}"

        elif "age distribution" in user_input:
            if "Age" in df.columns:
                mean_age = df["Age"].mean()
                std_age = df["Age"].std()
                return f"The age column has a mean of {mean_age:.2f} and a standard deviation of {std_age:.2f}."
            else:
                return "The dataset does not contain an 'Age' column."

        elif "bmi" in user_input:
            if "Body Mass Index" in df.columns:
                mean_bmi = df["Body Mass Index"].mean()
                min_bmi = df["Body Mass Index"].min()
                max_bmi = df["Body Mass Index"].max()
                return f"The Body Mass Index (BMI) has a mean of {mean_bmi:.2f}, a minimum of {min_bmi}, and a maximum of {max_bmi}."
            else:
                return "The dataset does not contain a 'Body Mass Index' column."

        elif "exit" in user_input:
            return "Goodbye! Thank you for using the chatbot."

        else:
            return "Sorry, I don't understand that. Please ask about 'columns', 'summary', 'missing values', 'age distribution', or 'bmi'."

    # Streamlit page layout
    st.set_page_config(page_title="Dataset Chatbot", page_icon="🤖", layout="wide")
    st.title("Dataset Chatbot")

    # Chat interface
    st.markdown("### Chat with the bot! (not functional as intended)")
    st.text("Type your question about the dataset below.")

    # Input box for user questions
    user_input = st.text_input("You:", key="input_box")

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Process user input
    if user_input and st.button("Send"):
        # Get the response and store the conversation
        response = chatbot_response(user_input, df)
        st.session_state.conversation.append({"user": user_input, "bot": response})

    # Display conversation
    st.markdown("### Conversation")
    for exchange in st.session_state.conversation:
        st.markdown(f"**You:** {exchange['user']}")
        st.markdown(f"**Bot:** {exchange['bot']}")
