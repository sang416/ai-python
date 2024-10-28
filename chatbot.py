import streamlit as st
from langchain_openai import OpenAI

# from dotenv import load_dotenv
# import os

# .env 파일에서 환경 변수 로드
# load_dotenv()

# OpenAI LLM 모델 초기화
llm = OpenAI()

# Streamlit 앱 설정
st.set_page_config(layout="wide")
st.title("Python Chatbot")

# 대화 기록 초기화
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# 대화 내용 표시
st.header("대화 내용")
for message in st.session_state.conversation:
    st.write(message)

# ... 기존 코드 ...

# 사용자 입력
user_input = st.text_input("메시지를 입력하세요:", key="user_input")

# 사용자 입력 처리 및 응답 생성
def handle_input():
    if st.session_state.user_input:
        response = llm(st.session_state.user_input)
        # 대화 기록에 추가
        st.session_state.conversation.append(f"You: {st.session_state.user_input}")
        st.session_state.conversation.append(f"Bot: {response}")
        # 입력 필드 초기화
        st.session_state.user_input = ""

        # 파이썬 코드의 들여쓰기를 유지하기 위해 코드 블록을 감싸기
        if "```" in response:
            response = response.replace("```", "```\n")

if st.button("전송", on_click=handle_input):
    pass

# ... 기존 코드 ...