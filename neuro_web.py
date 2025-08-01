import streamlit as st
from neuro_link import get_ai_response  # Use the function from your other file

st.title("🤖 NeuroLink - AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Say something to NeuroLink...")

if user_input:
    st.chat_message("user").write(user_input)

    ai_reply = get_ai_response(user_input)
    st.chat_message("assistant").write(ai_reply)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", ai_reply))
