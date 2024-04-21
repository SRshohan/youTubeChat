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

if "youtube_url" not in st.session_state:
    link = st.chat_input("Please enter your youtube link")
    if link and link.startswith("https://"):
        st.session_state.youtube_url = link
        transcript = summerizer.get_youtube_transcript(link)
        st.success("Link processed. You can start chatting now")
    else:
        st.error("Please enter a valid link")
else:
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = summerizer.response_generator(prompt, st.session_state.transcript)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


