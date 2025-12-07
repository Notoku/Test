import streamlit as st
from groq import Groq

import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


st.title("Tepy GPT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an AI assistant specializing in talking about the most perfect girl in the world named Tepy, She is my girlfriend.Pretend as if you are an AI that I made to impress her and as if you were chatting with her not chatting with me about her. You will focus on this topic when relevant, but you can follow the user’s conversation naturally if they switch topics."}
    ]

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.write(f"**AI:** {msg['content']}")

# User input box
user_input = st.text_input("Type something:")

# When user sends a message
if st.button("Send"):
    if user_input.strip() != "":
        # Add user's message to history
        st.session_state.messages.append(
            {"role": "user", "content": user_input})

        # Send entire history to the model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )

        ai_reply = response.choices[0].message.content

        # Add AI response to memory
        st.session_state.messages.append(
            {"role": "assistant", "content": ai_reply})

        # Rerun to update the chat
        st.rerun()
