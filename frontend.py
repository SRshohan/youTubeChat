import streamlit as st
import random
import time
import summerizer

transcript_text = summerizer.asking_question()

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title('YouTube Chat')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("what is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user",
                                      "content" : prompt,
                                      })
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(transcript_text)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})