import streamlit as st
import subprocess

MODEL = "phi3:mini"

st.set_page_config(page_title="ChatSUAS", page_icon="🤖")
st.title("🤖 ChatSUAS (modo rápido)")
st.caption("Modelo local leve — respostas curtas")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Pergunte algo sobre o SUAS")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
SUAS NÃO É SUS.
Responda em até 5 linhas.
Pergunta: {user_input}
"""

    with st.spinner("Pensando..."):
        result = subprocess.run(
            ["ollama", "run", MODEL, prompt],
            capture_output=True,
            text=True
        )

    response = result.stdout.strip() or "⚠️ Sem resposta do modelo."

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
