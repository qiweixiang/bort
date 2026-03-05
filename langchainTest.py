from collections.abc import Sequence
from sys import prefix
from typing import List

from langchain_classic.chains.constitutional_ai.prompts import examples
from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model="qwen-max", api_key='sk-4e9216382336465a9c8ce0120806c4ec')
# # 流式输出
## res = model.stream("你是谁。")

# # langchain 的流失输出
# for re in res:
#     print(re, end="", flush=True)
from langchain_classic.chains.question_answering.map_reduce_prompt import messages
from langchain_core.documents import Document
from langchain_core.messages import AIMessage
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import HumanMessage, SystemMessage
#
# model = ChatTongyi(model="qwen-max", api_key='sk-4e9216382336465a9c8ce0120806c4ec')
# messages = [
#     SystemMessage(content="你是一个唐朝的诗人。时运不济，自己写，别抄"),
#     HumanMessage(content="给我写一首诗吧")
# ]
#
# res = model.stream( messages)
# for re in res:
#     print(re.content, end="", flush=True)

# from langchain_community.embeddings import DashScopeEmbeddings
#
# st = DashScopeEmbeddings()
# # 将文本向量化 [-3.02587890625, 3.3109374046325684, 4.410546779632568, 0.4593261778354645, -4.43798828125, 0.844921886920929.......]
# print(st.embed_query("我喜欢你"))


# from langchain_core.prompts import PromptTemplate
#
# model = Tongyi(model='qwen-max')
# template = PromptTemplate.from_template("我叫{name},帮我孩子取个名字")
# template_text = template.format(name = '张伟')
#
# print(model.invoke(template_text))

# from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
# from langchain_community.llms.tongyi import Tongyi
# example = PromptTemplate.from_template("单词:{word},反义词:{any}")
# # FewShotPromptTemplate  提供少量的示例给大模型
# example_data = [{"word":"大", "any":"小"}, {"word":"小", "any":"大"}]
# few_sh = FewShotPromptTemplate(example_prompt=example, #示例数据模版
#                       examples=example_data, #示例数据
#                       prefix="请告诉我输入词的反义词，这是示例",    #示例之前的提示词
#                       suffix="告诉我{input_word}的反义词，如果你知道就按格式返回，如果你不知道或者不确定就返回不知道三个字就行，不用说别的任何话",
#                       input_variables=['input_word'])
#
# # few_text = few_sh.invoke(input={"c":"前"}).to_string()
# few_text = few_sh.format(input_word="你妈")
# print(few_text)
#
# model = Tongyi(model='qwen-max')
# print(model.invoke(few_text))


# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_community.llms.tongyi import Tongyi
# chat_yem = ChatPromptTemplate.from_messages([
#     {"role": "system", "content": "你是一个诗人"},
#     MessagesPlaceholder("history"),
#     {"role": "human", "content": "再来一首"}
# ])
# history_data = [
#     {"role": "human", "content": "写一首诗"},
#     {"role": "assistant", "content": "白日依山尽，黄河入海流，欲穷千里目，更上一层楼。"}
# ]
# text = chat_yem.invoke(input={"history":history_data}).to_string()
# model = Tongyi(model='qwen-max')
# shi = model.invoke(text)
# history_data.append({"role": "assistant", "content": shi})
# print(shi)

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_community.chat_models.tongyi import ChatTongyi
# chat_yem = ChatPromptTemplate.from_messages([
#     {"role": "system", "content": "你是一个诗人"},
#     MessagesPlaceholder("history"),
#     {"role": "human", "content": "再来一首"}
# ])
# history_data = [
#     {"role": "human", "content": "写一首诗"},
#     {"role": "assistant", "content": "白日依山尽，黄河入海流，欲穷千里目，更上一层楼。"}
# ]
# # text = chat_yem.invoke(input={"history":history_data}).to_string()
# model = ChatTongyi(model='qwen-max')
#
# # 组成一个链  这个链并不会执行
# chain = chat_yem | model | model
#
# #当你调用 chain.invoke(输入) 时，首先会把输入传给 chat_yem
# # chain.invoke() 这个链开始执行
# # print(chain.invoke(input={"history": history_data}))
# # shi = model.invoke(text)
# for chunk in chain.stream({"history": history_data}):
#     print(chunk.content, end="")


# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.output_parsers import StrOutputParser
# chat_yem = ChatPromptTemplate.from_messages([
#     {"role": "system", "content": "你是一个诗人"},
#     MessagesPlaceholder("history"),
#     {"role": "human", "content": "再来一首"}
# ])
# history_data = [
#     {"role": "human", "content": "写一首诗"},
#     {"role": "assistant", "content": "白日依山尽，黄河入海流，欲穷千里目，更上一层楼。"}
# ]
# # text = chat_yem.invoke(input={"history":history_data}).to_string()
# model = ChatTongyi(model='qwen-max')
# print(type(model))
# ChatTongyi
# so = StrOutputParser()
# # 组成一个链  这个链并不会执行
# chain = chat_yem | model | so | model
# #当你调用 chain.invoke(输入) 时，首先会把输入传给 chat_yem
# # chain.invoke() 这个链开始执行
# # print(chain.invoke(input={"history": history_data}))
# # shi = model.invoke(text)
# for chunk in chain.stream({"history": history_data}):
#     print(chunk.content, end="")

# def getName(a):
#     print(type(a))
#     print(a.content)
#     return {"name" : a.content}
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
# from langchain_core.runnables import RunnableLambda
#
# # p1 = PromptTemplate.from_template("我姓{name}，刚生了孩子，性别:{gener},帮我取个名字, 给我输出一个json，key:name，value是名字")
# p1 = PromptTemplate.from_template("我姓{name}，刚生了孩子，性别:{gener},帮我取个名字, 取个大气点的，直接输出名字")
# p2 = PromptTemplate.from_template("帮我解读一下名字:{name}的含义")
#
# # text = chat_yem.invoke(input={"history":history_data}).to_string()
# model = ChatTongyi(model='qwen-max')
# so = StrOutputParser()
# js = JsonOutputParser()
# ru = RunnableLambda(getName)
#
# # 组成一个链  这个链并不会执行
# chain = p1 | model | ru | p2 | model
# #当你调用 chain.invoke(输入) 时，首先会把输入传给 chat_yem
# # chain.invoke() 这个链开始执行
# # print(chain.invoke(input={"history": history_data}))
# # shi = model.invoke(text)
# # print(chain.invoke({"name": "祁", "gener": "女"}).content)
# for chunk in chain.stream({"name": "祁", "gener":"女"}):
#     print(chunk.content, end="")


# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
# from langchain_core.runnables import RunnableLambda
# from langchain_core.messages import BaseMessage
# import json
# import os
# from langchain_core.messages import messages_from_dict, message_to_dict
#
#
# class FileChatMessageHistory(BaseChatMessageHistory):
#     storage_path: str
#     session_id: str
#
#     def __init__(self, storage_path: str, session_id: str):
#         self.storage_path = storage_path
#         self.session_id = session_id
#
#     @property
#     def messages(self) -> list[BaseMessage]:
#         print("路径 :", self.storage_path, self.session_id, os.path.join(self.storage_path))
#         try:
#             with open(
#                 os.path.join(self.storage_path),
#                 "r",
#                 encoding="utf-8",
#             ) as f:
#                 messages_data = json.load(f)
#             return messages_from_dict(messages_data)
#         except FileNotFoundError:
#             return []
#
#     def add_messages(self, messages: Sequence[BaseMessage]) -> None:
#         all_messages = list(self.messages)  # Existing messages
#         all_messages.extend(messages)  # Add new messages
#
#         serialized = [message_to_dict(message) for message in all_messages]
#         file_path = os.path.join(self.storage_path)
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         with open(file_path, "w", encoding="utf-8") as f:
#             json.dump(serialized, f)
#
#     def clear(self) -> None:
#         file_path = os.path.join(self.storage_path)
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         with open(file_path, "w", encoding="utf-8") as f:
#             json.dump([], f)
#
#
# # fcm = FileChatMessageHistory("user_oo1", "./session.json")
#
# # prompt = PromptTemplate.from_template("你要根据历史会话来回答用户问题,历史对话:{chat_history},用户提问:{question},请回答")
#
# cpt = ChatPromptTemplate(
#     [
#         ("system", "你要根据历史会话来回答用户问题"),
#         MessagesPlaceholder("chat_history"),
#         ("human", "{question},请回答")
#     ]
# )
# model = ChatTongyi(model='qwen-max')
# stro = StrOutputParser()
# def printpt(pt):
#     print("提示词: ", pt.to_string())
#     return pt
# printpt = RunnableLambda(printpt)
#
# chain = cpt | printpt | model | stro
#
# store = {}
# def get_histroy(session_id):
#     if session_id not in store:
#         # 基于文件的本地存储
#         store[session_id] = FileChatMessageHistory(f"./mysession/{session_id}.json", session_id)
#     return store[session_id]
#
# # 带有记忆功能的 Runnable
# runs = RunnableWithMessageHistory(
#     chain,               #原始链
#     get_histroy,          #根据sesession_id获取历史会话 这个很重要的设计
#     input_messages_key = "question",   #当前问题的key
#     history_messages_key="chat_history"  #历史会话的key
# )
#
#
#
#
# if __name__ == '__main__':
#     session_config = {
#         "configurable":{
#             "session_id":"user_oo1"
#         }
#     }
#
#     print(runs.invoke({"question": "小明有一只猫"}, config=session_config))
#     print("======")
#     print(runs.invoke({"question": "小明有两只狗只猫"}, config=session_config))
#     print("======")
#     print(runs.invoke({"question": "小明有一共有几只宠物"}, config=session_config))


# from langchain_community.document_loaders import CSVLoader
#
#
# # file_path: Union[str, Path],
# #         source_column: Optional[str] = None,
# #         metadata_columns: Sequence[str] = (),
# #         csv_args: Optional[Dict] = None,
# #         encoding: Optional[str] = None,
# #         autodetect_encoding: bool = False,
# #         *,
# #         content_columns: Sequence[str] = (),
# csvload = CSVLoader(
#     file_path="./csv/aa.csv",
#     csv_args={
#         "delimiter": ","
#     },
#     encoding="utf-8"
# )
#
# # doc = csvload.load()
# # for e in doc:
# #     print(e.page_content)
#
# # 懒加载  取一个哪一个
# doc = csvload.lazy_load()
# for e in doc:
#     print(e.page_content)
# from langchain_community.document_loaders import CSVLoader,JSONLoader
#
#
# js_load = JSONLoader(
#     file_path="./session/2026-02-11_10_09_36.json",
#     jq_schema=".message[].role",
#     text_content=False,    #抽取的内容不是字符串
#     json_lines=False
# )
#
# doc = js_load.load()
# for e in doc:
#     print(e.page_content)

# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
#
#
# text_load = TextLoader(
#     file_path="./wenben/xiangyu.md",
#     encoding="utf-8"
# )
#
# doc_ = text_load.load()
#
# # for e in text_load.lazy_load():
# #     print(e)
#
# #文档分割器对象
# re = RecursiveCharacterTextSplitter(
#     chunk_size=1000,     #分段最大字符数
#     chunk_overlap=0,     # 分段重叠字符数
#     length_function=len,
#     separators=['\n\n','\n']
# )
#
# for split_document in re.split_documents(doc_):
#     print(split_document.page_content)
#     print("==============")

# from langchain_community.document_loaders import PyPDFLoader
#
# pyd = PyPDFLoader(file_path="C:\\Users\\60566\\Desktop\\B2C OCC Account Management REVISED 12-5-2025.pdf")
#
# i = 0
# for e in pyd.lazy_load():
#     i += 1
#     print(e)
#     print("===========", i)

from langchain_core.vectorstores import InMemoryVectorStore
# from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_community.document_loaders import CSVLoader
# from langchain_chroma import Chroma
#
#
# csv_laod = CSVLoader(
#     file_path="./csv/bb.csv",
#     encoding="utf-8",
#     source_column="source"
# )
#
# docs = csv_laod.load()
#
# # for doc in docs:
# #     print(doc.page_content)
#
# # 创建一个内存向量库 采用的 编码算法是DashScopeEmbeddings
# # vect = InMemoryVectorStore(
# #     embedding= DashScopeEmbeddings()
# # )
#
# # 这是本地基于sqllite的数据库进行持久化的
# vect = Chroma(
#     collection_name="test",
#     embedding_function=DashScopeEmbeddings(),
#     persist_directory="./chroma"
# )
#
# # 向这个内存向量库中添加文档和对应的 id
# # vect.add_documents(documents=docs,ids=["id"+str(i) for i in range(1, len(docs) +1)])
#
# # vect.delete(['id1'])
#
# # 通过向量库进行搜索，返回指定数目的文档
# result = vect.similarity_search(query="Python是不是简单易学啊", k=3, filter={"source":"黑马程序员"})
# for e in result:
#     print(e)
#     print("="*20)

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
# from langchain_core.runnables import RunnableLambda
# from langchain_core.messages import BaseMessage
# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import DashScopeEmbeddings
#
# # 文本加载器
# xianyu_text = TextLoader(
#     file_path="./wenben/xaingyubenji.txt",
#     encoding="utf-8"
# )
# docs = xianyu_text.load()
#
# # 内存式的向量库
# vect = InMemoryVectorStore(
#     embedding= DashScopeEmbeddings(model="text-embedding-v4")
# )
#
# # 文本分割器
# re = RecursiveCharacterTextSplitter(
#     chunk_size=500,     #分段最大字符数
#     chunk_overlap=50,     # 分段重叠字符数
#     length_function=len,
#     separators=['。', '，', ' ']
# )
#
# # 按照指定规则分隔文本
# all_docs = re.split_documents(docs)
# for all_doc in all_docs:
#     print(all_doc.page_content)
#     print("="*30)
#
# # 向向量库中添加分隔好的文本
# vect.add_documents(documents=all_docs,ids=["id"+str(i) for i in range(1, len(all_docs) +1)])
#
#
# # for e in result:
# #     print(e.page_content)
# #     print("="*20)
#
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你要根据我给你的文档为主来回答用户问题，， 文档的内容是:{context}"),
#     ("human", "{question},请回答")
# ])
# model = ChatTongyi(model='qwen-max')
#
# def get_prompt(a):
#     print("提示词:", a)
#     return a
#
# chain = prompt | get_prompt | model | StrOutputParser()
#
# # 从向量库中根据用户输入搜索出相应的文档
# result = vect.similarity_search(query="范增是谁", k=1)
# # 将用户输入和搜索到的文档传入模型进行推理
# print(chain.invoke({"question": "范增是谁", "context": result[0].page_content}))

# 以上就是RAG的基本流程


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.messages import BaseMessage
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings

# 文本加载器
xianyu_text = TextLoader(
    file_path="./wenben/xaingyubenji.txt",
    encoding="utf-8"
)
docs = xianyu_text.load()

# 内存式的向量库
vect = InMemoryVectorStore(
    embedding= DashScopeEmbeddings(model="text-embedding-v4")
)

# 文本分割器
re = RecursiveCharacterTextSplitter(
    chunk_size=500,     #分段最大字符数
    chunk_overlap=50,     # 分段重叠字符数
    length_function=len,
    separators=['。', '，', ' ']
)

# 按照指定规则分隔文本
all_docs = re.split_documents(docs)
# for all_doc in all_docs:
#     print(all_doc.page_content)
#     print("="*30)

# 向向量库中添加分隔好的文本
vect.add_documents(documents=all_docs,ids=["id"+str(i) for i in range(1, len(all_docs) +1)])


# for e in result:
#     print(e.page_content)
#     print("="*20)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你要根据我给你的文档为主来回答用户问题，， 文档的内容是:{context}"),
    ("human", "{question},请回答")
])
model = ChatTongyi(model='qwen-max')

def get_prompt(a):
    print("提示词:", a)
    return a

# 这是我自定义的入链方式
# def optainPrompt(question :str):
#     result = vect.similarity_search(query=question, k=1)
#     if not result:
#         return {"question": question, "context": "没有相关文档"}
#     context = []
#     for doc in result:
#         context.append(doc.page_content)
#     return {"question": question, "context": context}
#
# printpt = RunnableLambda(optainPrompt)
#
# #
#
# # 通过这种方法可以让向量库检索入链
# chain = printpt | prompt | get_prompt | model | StrOutputParser()

# 从向量库中根据用户输入搜索出相应的文档

# 将向量库检索组成可入链的形式  即变为Runnable的实现

def getpromot(docs :List[ Document]):
    if not docs:
        return ['没有相关文档']
    context = []
    for doc in docs:
        context.append(doc.page_content)
    return context

# RunnablePassthrough这个东西我不太理解  相当于一个占位的吧chain.stream("项羽是谁") 将数据传给RunnablePassthrough，然后RunnablePassthrough又将传入的数据原封不动的传给下一个节点
retriever = vect.as_retriever(search_kwargs={"k": 1})
chain = {
            "question":RunnablePassthrough(),
            "context": retriever | getpromot
        } | prompt | get_prompt | model | StrOutputParser()

# 将用户输入和搜索到的文档传入模型进行推理
for e in chain.stream("项羽是谁"):
    print(e, end="")