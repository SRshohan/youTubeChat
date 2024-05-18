import streamlit as st
import backend

st.title("YouTube ChatBot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "youtube_link" not in st.session_state:
    st.session_state.youtube_link = None
if "transcript" not in st.session_state:
    st.session_state.transcript = None


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


if prompt := st.chat_input("Ask any question"):
    # Add user message to the chat history
    st.session_state.messages.append({"role" : "user", "content" : prompt})

    # Display user message to the chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream()

    st.session_state.messages.append({"role" : "assistant", "content" : response})


    

