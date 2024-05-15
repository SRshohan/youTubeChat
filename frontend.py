import streamlit as st
import summerizer

st.title("YouTube ChatBot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "youtube_link" not in st.session_state:
    st.session_state.youtube_link = None
if "transcript" not in st.session_state:
    st.session_state.transcript = None

# Asking for youtube link first if not already provided
for message in st.session_state:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

