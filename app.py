import streamlit as st
import openai
import os

# Load API key from Streamlit secrets or environment
openai.api_key = os.getenv("OPENAI_API_KEY", "")

st.set_page_config(page_title="NHAI Chatbot", page_icon="🚦")
st.title("NHAI AI Assistant 🚦")
st.write("Ask me anything related to AI or infrastructure!")

# Input box
user_input = st.text_input("You:")

if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("**Bot:**", response["choices"][0]["message"]["content"])
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Make sure you set your OPENAI_API_KEY properly.")
