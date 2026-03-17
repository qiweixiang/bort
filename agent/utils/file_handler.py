import os

from kubernetes.client import ApiException
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

from agent.utils.logger_handler import logger
from agent.utils.path_tool import get_abs_path
import hashlib

def get_file_md5_hex(file_path :str) -> str:

    if not os.path.exists(file_path):
        logger.error(f"get_file_md5_hex错误，文件路径{file_path}不存在")
    if not os.path.isfile(file_path):
        logger.error(f"get_file_md5_hex错误，文件路径{file_path}不是文件")

    block_size = 4096

    try :
        md5_obj = hashlib.md5()
        with open(file_path, "rb") as f:
            while True:
                block = f.read(block_size)
                if not block:  # 读取完毕
                    break
                md5_obj.update(block)  # 逐块更新哈希
        return md5_obj.hexdigest()
    except Exception as e:
        logger.error(f"计算Md5值失败，文件路径{file_path}")
        raise ApiException("计算MD5失败")


def listdir_with_allowed_type(path : str, allowed_types : tuple[ str]):
    if not os.path.isdir(path):
        raise ApiException("传入的路径不是文件夹")

    files = []
    for f in os.listdir(path):
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))

    return  files

def load_pdf(pdf_file_path, password=None) -> list[Document]:
    return PyPDFLoader(file_path=pdf_file_path, password=password).load()


def load_txt(txt_file_path) -> list[Document]:
     return TextLoader(
        file_path=txt_file_path,
        encoding="utf-8"
    ).load()

if __name__ == '__main__':
    # print(get_file_md5_hex(get_abs_path(("config/agent.yml"))))
    print(listdir_with_allowed_type(get_abs_path(("config")), ('yml')))