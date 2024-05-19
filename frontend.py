import streamlit as st
import backend

st.title("YouTube ChatBot")

youtube_link = st.sidebar.text_input("youtube_link")

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

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not youtube_link.startswith("https://"):
        st.warning('Please enter valid youtube link!', icon='⚠')


    if submitted and youtube_link.startswith("https://"):
        transcript = backend.youtube_transcript(youtube_link)
        store_data = backend.storing_data_for_transcript(transcript)
        if prompt := st.chat_input("Ask any question"):
            # Add user message to the chat history
            st.session_state.messages.append({"role" : "user", "content" : prompt})

            # Display user message to the chat container
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = st.write_stream(backend.load_llm(prompt))

            st.session_state.messages.append({"role" : "assistant", "content" : response})


    

