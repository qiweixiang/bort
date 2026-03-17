import os.path

from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from agent.utils.config_handler import chroma_yml
from agent.model.factory import chat_model, embedd_model
from agent.utils.path_tool import get_abs_path
from agent.utils.file_handler import listdir_with_allowed_type, get_file_md5_hex, load_pdf, load_txt
from agent.utils.logger_handler import logger


class VectorStoreService:
    def __init__(self):
        # 定义一个本地向量库
        self.vector = Chroma(
            collection_name=chroma_yml['collection_name'],  # 向量库表明
            embedding_function=embedd_model,  # 向量模型
            persist_directory=chroma_yml['persist_directory']  # 持久化目录
        )

        # chunk_size: 200
        # chunk_overlap: 20
        # separators: ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
        # 定义一个文档分割器
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chroma_yml['chunk_size'],  # 分段最大字符数
            chunk_overlap=chroma_yml['chunk_overlap'],  # 分段重叠字符数
            length_function=len,
            separators=chroma_yml['separators']
        )

    def get_reriever(self):
        return self.vector.as_retriever(search_kwargs={"k": chroma_yml['k']})


    def check_md5_hex(self, md5_check):
        """
        检查传入的MD5是否存在
        :param md5_check:
        :return:
        """
        if not os.path.exists(get_abs_path(chroma_yml['md5_hex_store'])):
            open(get_abs_path(chroma_yml['md5_hex_store']), encoding="utf-8", mode="w").close()
            return False

        with open(get_abs_path(chroma_yml['md5_hex_store']), encoding="utf-8", mode="r") as file:
            for line in file:
                line = line.strip()
                if line == md5_check:
                    return True
        return False


    def save_md5(self, md5_add):
        with open(get_abs_path(chroma_yml['md5_hex_store']), encoding="utf-8", mode="w") as file:
            file.write(md5_add + "\n")

    def get_file_documents(self, file_path) -> list[Document]:
        if file_path.endswith(".pdf"):
            return load_pdf(file_path)
        elif file_path.endswith(".txt"):
            return load_txt(file_path)


    def load_file_documents(self):
        for file_path in listdir_with_allowed_type(get_abs_path(chroma_yml['data_path']), tuple(chroma_yml['allow_knowledge_file_type'])):
            file_md5 = get_file_md5_hex(file_path)
            if self.check_md5_hex(file_md5):
                logger.warn(f"加载知识库，文件{file_path}已经存在，请勿重复上传")
                continue
            try:
                file_documents = self.get_file_documents(file_path)
                if not file_documents:
                    logger.warn(f"加载知识库，文件{file_path}文档为空")
                    continue

                final_documents = self.splitter.split_documents(file_documents)
                if not final_documents:
                    logger.warn(f"加载知识库，文件{file_path}文档分段为空")
                    continue


                #保存文档
                self.vector.add_documents(final_documents)

                #保存md5
                self.save_md5(file_md5)

                logger.info(f"加载知识库:{file_path}成功")
            except Exception as e:
                logger.error(f"加载知识库:{file_path}失败", exc_info=True)
                raise e


if __name__ == '__main__':
    vec =  VectorStoreService()
    # vec.load_file_documents()

    rec = vec.get_reriever()
    for i in rec.invoke("迷路"):
        print(i.page_content)