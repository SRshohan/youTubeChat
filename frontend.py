import streamlit as st
import backend
import asyncio

st.title("YouTube ChatBot")

# Sidebar input for YouTube link
youtube_link = st.sidebar.text_input("YouTube Link")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "youtube_link" not in st.session_state:
    st.session_state.youtube_link = None
if "transcript" not in st.session_state:
    st.session_state.transcript = None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Form to input text and submit
with st.form('my_form'):

    submitted = st.form_submit_button('Submit')

    # Validate YouTube link
    if not youtube_link.startswith("https://"):
        st.warning('Please enter a valid YouTube link!', icon='⚠')
    elif submitted and youtube_link.startswith("https://"):
        st.session_state.youtube_link = youtube_link
        transcript = backend.youtube_transcript(youtube_link)
        st.session_state.transcript = transcript
        store_data = backend.storing_data_for_transcript(transcript)
        st.success("Transcript loaded and stored successfully!")

# Chat input
if prompt := st.chat_input("Ask any question"):
    # Add user message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in the chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    llm_response = asyncio.run(backend.load_llm(prompt))
    # Process the user's input and get the response from the backend
    response = backend.storing_data_of_user(llm_AI_message=llm_response)

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




    

