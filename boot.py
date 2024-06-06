
import streamlit as st
import pyttsx3

st.markdown(
    """
    <style>
    .title {
        text-align: left;
        font-size: 3em;
        margin-top: 20px;
        margin-bottom: 20px;
    }""",
    unsafe_allow_html=True
)
# Display the title
st.markdown('<div class="title">Echo Bot</div>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = prompt
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Initialize TTS engine
    engine = pyttsx3.init()
    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Speak the response
    engine.say(response)
    engine.runAndWait()
