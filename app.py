import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("Chatbox")
st.write("Ask anything!")

# User input
user_input = st.text_input("Enter your question:")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Thinking..."):
            response = llm.invoke(user_input)
            st.success(response.content)
    else:
        st.warning("Please enter a question!")