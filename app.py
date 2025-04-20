import streamlit as st
from dotenv import load_dotenv
from src.chain import create_chain

# Load API key from .env
load_dotenv()

st.set_page_config(page_title="Sage the AI Therapist", page_icon="🧠")
st.title("🧠 Sage - Your Virtual Therapist")

# Session state
if "chain" not in st.session_state:
    st.session_state.chain = create_chain()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat form
user_input = st.chat_input("What's on your mind today?")
if user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Sage", response))

# Display chat
for sender, message in st.session_state.chat_history:
    with st.chat_message("assistant" if sender == "Sage" else "user"):
        st.markdown(message)
