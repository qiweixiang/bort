from abc import ABC, abstractmethod
from typing import Optional

from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms.tongyi import Tongyi
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from ..utils.config_handler import rag_yml


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[BaseChatModel | Embeddings]:
        pass


class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[BaseChatModel | Embeddings]:
        return ChatTongyi(model=rag_yml['chat_model_name'])

class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[BaseChatModel | Embeddings]:
        return DashScopeEmbeddings(model=rag_yml['embedding_model_name'])


chat_model = ChatModelFactory().generator()
embedd_model = EmbeddingsFactory().generator()