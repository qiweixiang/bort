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
                   chain,                               #原始链
                   FileChatMessageHistory.get_history,                    #根据sesession_id获取历史会话 这个很重要的设计
                   input_messages_key = input_messages_key,     #当前问题的key
                   history_messages_key= history_messages_key  #历史会话的key
               )

    @staticmethod
    def get_history(session_id):
        print("get_history", session_id)
        store = {}
        if session_id not in store:
            # 基于文件的本地存储
            store[session_id] = FileChatMessageHistory(f"./mysession/{session_id}.json", session_id)
        return store[session_id]


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

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)  # Existing messages
        all_messages.extend(messages)  # Add new messages

        print("add_messages", self.storage_path)
        serialized = [message_to_dict(message) for message in all_messages]
        file_path = os.path.join(self.storage_path)
        print("file_path", file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def clear(self) -> None:
        file_path = os.path.join(self.storage_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)