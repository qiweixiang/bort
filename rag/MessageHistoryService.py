import json
import os
from datetime import datetime
from typing import Sequence
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, messages_from_dict, message_to_dict
from langchain_core.runnables import RunnableWithMessageHistory


class FileChatMessageHistory(BaseChatMessageHistory):
    storage_path: str
    session_id: str

    def __init__(self, storage_path: str, session_id: str):
        print("__init__", storage_path)
        self.storage_path = storage_path
        self.session_id = session_id


    def get_memory_chain(self, chain, input_messages_key, history_messages_key):
        return RunnableWithMessageHistory(
                   chain,                                      #原始链
                   FileChatMessageHistory.get_history,         #根据sesession_id获取历史会话 这个很重要的设计
                   input_messages_key = input_messages_key,    #当前问题的key  也就是说调用这个链的时候传入的参数：例如  invoke({"question":"小明有一个苹果"}
                   history_messages_key= history_messages_key  #历史会话的key   这是把历史会话封装在这个key里面
               )

    # 获取历史会话
    @staticmethod
    def get_history(session_id):
        store = {}
        if session_id not in store:
            # 基于文件的本地存储 创建一个基于文件的会话存储
            store[session_id] = FileChatMessageHistory(f"./mysession/{session_id}.json", session_id)
        return store[session_id]

    # 获取历史会话
    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(
                os.path.join(self.storage_path),
                "r",
                encoding="utf-8",
            ) as f:
                messages_data = json.load(f)
            return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    # 添加历史会话
    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)  # Existing messages
        all_messages.extend(messages)  # Add new messages

        serialized = [message_to_dict(message) for message in all_messages]
        file_path = os.path.join(self.storage_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def clear(self) -> None:
        file_path = os.path.join(self.storage_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)