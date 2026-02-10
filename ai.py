import os
from openai import OpenAI

# 调用deepseek api
client = OpenAI(
    api_key='sk-088d1435f3fc43079010da5e0cb82c96',
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        # {"role": "system", "content": "你是一个数学家"},
        # {"role": "user", "content": "十二个苹果分给三个人怎么均分"},
        # {"role":"assistant", "content":"这是一个简单的除法问题。  \n\n**计算过程：**  \n\\[\n\\frac{12}{3} = 4\n\\]  \n\n**答案：**  \n每人分得 **4 个苹果**。"},
        # {"role": "user", "content": "那两个人呢"},
        # {"role":"assistant", "content":"如果 **12 个苹果分给 2 个人**，计算如下：  \n\n\\[\n\\frac{12}{2} = 6\n\\]  \n\n**答案：**  \n每人分得 **6 个苹果**。"},
        # {"role": "user", "content": "那四个人呢"},

        {"role": "system", "content": "你是一个喜剧演员，回答的幽默风趣一点"},
        {"role": "user", "content": "怎么评论现在的电车的电池"},
    ],
    stream=True
)

# 这是流失输出
for chunk in response:
    # 每个 chunk 是一个 ChatCompletionChunk 对象
    delta = chunk.choices[0].delta
    if delta.content:
        print(delta.content, end="", flush=True)  # 实时打印
print(response.json())
print(response.choices[0].message.content)

# from ollama import chat
# from ollama import ChatResponse
#
# response: ChatResponse = chat(model='deepseek-r1:8b', messages=[
#   {"role": "system", "content": "你是一个数学家"},
#   {"role": "user", "content": "十二个苹果分给三个人怎么均分"},
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)