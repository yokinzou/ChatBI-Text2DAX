import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

ai_key = os.getenv("deepseek_api_key")

def chatPBI():
    st.set_page_config( 
        page_title="Chat PBI",
        page_icon="logo.png",
        layout="wide")
   

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # 添加占位文本 "What is up?"
    if prompt := st.chat_input("What is up?"):
        client = ChatOpenAI(
            api_key=ai_key,
            base_url="https://api.deepseek.com/v1",
            model_name="deepseek-chat"
        )
        
        # 添加用户消息并显示
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 使用 with 语句块处理助手回复
        with st.chat_message("assistant"):
            response = client.invoke(st.session_state.messages)
            msg = response.content
            st.write(msg)
            st.session_state.messages.append({"role": "assistant", "content": msg})