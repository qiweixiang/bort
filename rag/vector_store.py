from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings


class VectorStoreService:
    def __init__(self):
        # 定义一下向量库
        self.vector_store = Chroma(
            collection_name="test", #向量库表明
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),  #向量模型
            persist_directory="./chroma" #持久化目录
        )

    def get_retriver(self):
        return self.vector_store.as_retriever(search_kwargs={"k": 1})

if __name__ == '__main__':
    vector_store = VectorStoreService()
    res = vector_store.get_retriver().invoke("新入职的试用期是多久")
    for re in res:
        print(re.page_content)
