import streamlit as st
from app import get_response

st.title("🤖 AI Chatbot")

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        answer = get_response(user_input)
        st.write(answer)
        