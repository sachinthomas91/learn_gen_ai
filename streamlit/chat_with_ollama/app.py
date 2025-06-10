import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2:7b"

st.set_page_config(page_title="Chat with Qwen2:7b", layout="centered")
st.title("💬 Qwen2 Chat (Local via Ollama Qwen2:7B)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        if response.ok:
            answer = response.json().get("response", "").strip()
        else:
            answer = "⚠️ Error: Could not get response from Ollama."

    st.session_state.chat_history.append({"role": "assistant", "content": answer})

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            st.markdown(f'<div style="text-align: right">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(msg["content"])
