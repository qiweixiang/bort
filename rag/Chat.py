import streamlit as st
from openai import OpenAI
import json
from datetime import datetime
from pathlib import Path
import os
import RagChatService

# st.set_page_config(
#     page_title="我的助手",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )

if "count" not in st.session_state:
    st.session_state.count = 0


if 'message' not in st.session_state:
    if os.path.exists(f"./mysession/user_oo1.json"):
        with open(f"./mysession/user_oo1.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            messages = []
            for chat_data_json in data:
                message = {}
                message['role'] = chat_data_json['type']
                message['content'] = chat_data_json['data']['content']
                messages.append(message)
        st.session_state['message'] = messages
    else:
        st.session_state['message'] = []


# 大标题
st.title("AI智能回复")
# st.logo("C:\\Users\\60566\\Desktop\\u=2892873496,2351386762&fm=253&gp=0.jpg")

session_config = {
    "configurable": {
        "session_id": "user_oo1"
    }
}

for i in st.session_state['message']:
    if i['role'] == 'user':
        st.chat_message("user").write(f"{i['content']}")
    else:
        st.chat_message("assistant").write(f"{i['content']}")

prompt = st.chat_input("请输入你想问的问题")

if 'service' not in st.session_state:
    st.session_state['service'] = RagChatService.RagService()

# 这里的字符串会自动转化为布尔值  看是否为空
if prompt:
    all = st.session_state['message']
    st.chat_message("user").write(f"{prompt}")
    d = {"role": "user", "content": prompt}
    all.append(d)

    rag = st.session_state['service']
    fullcontent = ""
    response_mesage = st.empty()
    for chunk in rag.get_chain('user_oo1').stream({"question": prompt}, config = session_config):
        # 每个 chunk 是一个 ChatCompletionChunk 对象
        if chunk:
            fullcontent += chunk
            response_mesage.chat_message("assistant").write(fullcontent)

    all.append({"role": "assistant", "content": fullcontent})

    st.session_state['message'] = all

    # st.session_state.count +=1
    st.rerun()
