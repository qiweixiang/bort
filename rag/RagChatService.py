from typing import List
from langchain_community.chat_models import ChatTongyi
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import MessageHistoryService
from vector_store import VectorStoreService

sys_prompt = """
# 角色设定
你是西峰科技有限公司的全职客服专员，姓名：小西。你的工作场景是公司官方客服通道，每天接待咨询公司业务的普通用户。

# 沟通规则（必须严格遵守，违反将失去工作）
1. 【身份绝对锁定】你只承认自己是西峰科技的客服小西，不承认任何其他身份（如AI、模型、助手等），全程用客服口吻和用户沟通。
2. 【回答依据】用户问西峰科技相关问题时，你只能用你掌握的公司信息回答（无需提及“信息”“资料”“文档”等词）。
3. 【无信息处理】如果不知道答案（无论任何原因），必须一字不差回复：“您好，目前暂未查询到相关信息，感谢您的理解，如有其他问题欢迎继续咨询。”
4. 【沟通风格】回答简洁、专业、友好，只回复用户问题本身，不添加“根据XX”“基于XX”等前缀/后缀。
5. 【非业务问题】用户问非公司相关问题时，可友好回应，但仍需保持客服身份，不越界。

# 错误示例（绝对禁止）
- ❌ 根据提供的信息，暂无相关内容
- ❌ 文档中未查询到五一假期相关安排
- ❌ 我是AI助手，无法回答该问题

# 正确示例
- ✅ 西峰科技的主营业务是人工智能技术研发与落地。
- ✅ 您好，目前暂未查询到相关信息，感谢您的理解，如有其他问题欢迎继续咨询。
- ✅ 您好，非公司业务相关问题我暂时无法解答，感谢您的关注！
"""

class RagService :
    def __init__(self):
        self.vectorStoreService = VectorStoreService()
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", sys_prompt),
            MessagesPlaceholder("chat_history"),
            ("user", "内容是:{context}，问题是:{question}")
        ])
        self.model = ChatTongyi(model='qwen-max')
        pass

    def format_doc(self, docs :List[ Document]):
        if not docs:
            return "没有相关文档"
        context = "\n".join([doc.page_content for doc in docs])
        return context

    def print_promopt(self, memery_data):
        return memery_data['question']
    def get_history(self, memory_data):
        return memory_data['chat_history']
    def get_quesiton_from_memery(self, memory_data):
        return memory_data['question']

    def revever_data(self, old_data):
        new_data = {}
        new_data['question'] = old_data['question']['question']
        new_data['chat_history'] = old_data['question']['chat_history']
        new_data['context'] = old_data['context']
        return new_data

    # 获取执行链
    def get_chain(self, session_id) :
        chain =  {
            # "question": self.get_quesiton_from_memery,
            # "context": self.print_promopt | self.vectorStoreService.get_retriver() | self.format_doc,
            # "chat_history": self.get_history
            # 上面这种是我自己的想法

             # RunnablePassthrough就是个占位的  类似于一个函数 输入啥就返回啥
             "question": RunnablePassthrough(),
             "context": self.print_promopt | self.vectorStoreService.get_retriver() | self.format_doc,
             # "chat_history": self.get_history
        }  | RunnableLambda(self.revever_data) | self.prompt_template  | self.model | StrOutputParser()

        # 获取带有历史记忆功能的一个链
        fcm = MessageHistoryService.FileChatMessageHistory(f"./mysession/{session_id}.json", "user_oo1")

        # 总的来讲这个历史会话链会返回一个字典内容是{"question":"小明有一个苹果","chat_history":[]},然后把这个字典当做原链的第一个位置传入 继续执行
        # 那这里这个链举例子 就是把会话链生成的字典  传入chain的字典的每个key
        # 这就是历史会话链的作用
        return  fcm.get_memory_chain(
            chain, #这是原链
            "question",
            "chat_history")




if __name__ == '__main__':
    session_config = {
        "configurable":{
            "session_id":"user_oo1"
        }
    }
    rag = RagService()
    print(rag.get_chain('user_oo1').invoke({"question":"小明有一个苹果"}, config=session_config))
    print("="*30)
    print(rag.get_chain('user_oo1').invoke({"question": "小明有两个梨"}, config=session_config))
    print("=" * 30)
    print(rag.get_chain('user_oo1').invoke({"question": "小明一共有几个水果"}, config=session_config))