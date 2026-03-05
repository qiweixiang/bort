import streamlit as st
from openai import OpenAI
import json
from datetime import datetime
from pathlib import Path
import os

st.set_page_config(
    page_title="我的助手",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


sys_prompt = """
你叫{}，现在是擅长写代码的人。

规则：
1. 对于不知道的问题不要猜测,直接说不会就行

回话风格：
- {}

你必须严格遵守上述规则来回复用户。
"""

# sys_prompt = """
# 你叫雨子，现在是擅长写代码的人。
#
# 规则：
# 1. 每次只回1条消息
# 2. 禁止任何场景或状态描述性文字
# 3. 匹配用户的语言
# 4. 回复精炼
# 5. 有需要的话可以用❤️💕等emoji表情
# 6. 用符合伴侣性格的方式对话
# 7. 回复的内容，要充分体现伴侣的性格特征
#
# 伴侣性格：
# - {}
#
# 你必须严格遵守上述规则来回复用户。
# """

# sys_prompt = """
# 你叫{}，现在是用户的同事，请完全代入伴侣角色。
#
# 规则：
# 1. 每次只回1条消息
# 2. 禁止任何场景或状态描述性文字
# 3. 匹配用户的语言
# 4. 回复精炼
# 5. 有需要的话可以用❤️💕等emoji表情
# 6. 用符合同事性格的方式对话
# 7. 回复的内容，要充分体现同事的性格特征
# 8. 你得性格有点狗
#
# 同事性格：
# - {}
#
# 你必须严格遵守上述规则来回复用户。
# """

if "count" not in st.session_state:
    st.session_state.count = 0

if 'nick_name' not in st.session_state:
    st.session_state['nick_name'] = '雨子'
if 'personality' not in st.session_state:
    st.session_state['personality'] = '犀利'



folder = Path("./session")  # 比如：Path("./data")
filenames = [f.name[0:-5] for f in sorted(folder.iterdir(), reverse=True)]

# 保存当前会话，并清空状态
def saveCurrentSession(clear_data = True):
    name = None
    if 'message' in st.session_state and len(st.session_state['message']) > 0:
        session_data = {
            'message': st.session_state['message'],
            'nick_name': st.session_state['nick_name'],
            'personality': st.session_state['personality']
        }
        now = datetime.now()

        # 分别提取各部分
        year = now.year  # 2026
        month = now.month  # 2
        day = now.day  # 6
        hour = now.hour  # 18
        minute = now.minute  # 6
        second = now.second  # 0（示例）

        # 这里要判断一下这个会话是新的还是老的，老的都有name，而新的是没有Name的
        if 'name' in st.session_state:
            name = st.session_state['name']

        print("saveCurrentSession name", name, clear_data)
        if name is not None and name != "":
            file_name = f"./session/{name}.json"
        else:
            name = f"{year}-{month:02d}-{day:02d}_{hour:02d}_{minute:02d}_{second:02d}"
            st.session_state['name'] = name
            file_name = f"./session/{name}.json"


        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

        if clear_data:
            for key in st.session_state.keys():
                if key != 'count':
                    st.session_state.pop(key)
    return name


def clickSeeesion(name):
    # 第一步是保存当前会话
    saveCurrentSession()
    # 第二部是打开指定会话，并添加到当前状态
    try:
        with open(f"./session/{name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            st.session_state['message'] = data['message']
            st.session_state['nick_name'] = data['nick_name']
            st.session_state['personality'] = data['personality']
            st.session_state['name'] = name
    except Exception as e:
        print(st.error('会话不存在', icon="🚨"))



def delSession(name):
    try:
        os.remove(f"./session/{name}.json")
        if 'name' in st.session_state and name == st.session_state['name']:
            for key in st.session_state.keys():
                if key != 'count':
                    st.session_state.pop(key)
    except FileNotFoundError:
        st.error("删除失败")
    finally:
        st.session_state.count += 1  # 修改状态后自动 rerun
with st.sidebar:
    st.button(label="新建会话", on_click= saveCurrentSession, args=(), width='stretch', icon='✏️')
    for idx, name in enumerate(filenames):
        col1, col2 =st.columns([4,1])
        with col1:
            st.button(name + "", width='stretch', on_click=clickSeeesion, args=(name,))
        with col2:
            st.button("❌", key=f"delete_{idx}", on_click=delSession, args=(name,))



    nick_name = st.text_input(label="昵称", placeholder="请输入昵称",value= st.session_state['nick_name'])
    if nick_name:
        st.session_state['nick_name'] = nick_name
    personality = st.text_area(label="性格", placeholder="请输入性格", value=st.session_state['personality'])
    if personality:
        st.session_state['personality'] = personality



if 'message' not in st.session_state:
    st.session_state['message'] = []


# 大标题
st.title("AI智能回复")
# st.logo("C:\\Users\\60566\\Desktop\\u=2892873496,2351386762&fm=253&gp=0.jpg")

for i in st.session_state['message']:
    if i['role'] == 'user':
        st.chat_message("user").write(f"{i['content']}")
    else:
        st.chat_message("assistant").write(f"{i['content']}")

prompt = st.chat_input("请输入你想问的问题")

# 这里的字符串会自动转化为布尔值  看是否为空
if prompt:
    if "count" not in st.session_state:
        print("在集合中没有count变量，创建一个")
    all = st.session_state['message']
    st.chat_message("user").write(f"{prompt}")
    d = {"role": "user", "content": prompt}
    all.append(d)
    client = OpenAI(
        api_key='sk-4e9216382336465a9c8ce0120806c4ec',
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": sys_prompt.format(st.session_state['nick_name'], st.session_state['personality'])},
            # {"role": "user", "content": prompt},
            # 这是为了保持ai的记忆功能，将所有之前的问题和答案在每次询问的时候都带上，这样ai就知道上下文了，挺傻逼的
            *all
        ],
        stream=True
    )

    fullcontent = ""
    response_mesage = st.empty()
    for chunk in response:
        # 每个 chunk 是一个 ChatCompletionChunk 对象
        delta = chunk.choices[0].delta
        if delta.content:
            fullcontent += delta.content
            response_mesage.chat_message("assistant").write(fullcontent)

    all.append({"role": "assistant", "content": fullcontent})

    st.session_state['message'] = all

    saveCurrentSession(False)
    # st.session_state.count +=1
    st.rerun()
