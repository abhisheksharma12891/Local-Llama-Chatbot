import streamlit as st
from langchain_community.llms import Ollama

# --- CONFIGURATION ---
st.set_page_config(page_title="Local Llama Chatbot 🦙", layout="centered")

def get_response(user_input):
    try:
        # Connect to Local Ollama
        llm = Ollama(model="llama3") 
        response = llm.invoke(user_input)
        return response
    except Exception as e:
        return f"Error: Ensure Ollama is running! ({str(e)})"

# --- UI ---
st.title("🦙 Chat with Llama 3 (Locally)")
st.caption("Powered by Ollama | No Internet Required 🚫")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display Chat History
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
if prompt := st.chat_input("Ask Llama something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Llama is thinking..."):
        response = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)