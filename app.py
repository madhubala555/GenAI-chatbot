import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="GenAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 GenAI Chatbot")
st.caption("Powered by Google Gemini")

if not API_KEY:
    st.error("GEMINI_API_KEY is missing. Add it to the .env file.")
    st.info("See README.md for setup instructions.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# Conversation history for the current browser session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Ask me anything...")

if user_prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Send the conversation to the Gemini model so it can use context.
    contents = []
    for message in st.session_state.messages:
        contents.append({
            "role": "user" if message["role"] == "user" else "model",
            "parts": [{"text": message["content"]}]
        })

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=contents
                )
                answer = response.text
                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
            except Exception as e:
                st.error(f"Something went wrong: {e}")

with st.sidebar:
    st.header("About")
    st.write(
        "This chatbot uses Generative AI through the Google Gemini API. "
        "It keeps the conversation history during the current session."
    )

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()
