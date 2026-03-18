

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from agent.rag.vetor_store import VectorStoreService
from agent.utils.prompt_loader import load_prompts
from agent.model.factory import chat_model


class RagSummarizeService:
    def __init__(self):
       self.vector = VectorStoreService()
       self.retriver = self.vector.get_reriever()
       self.prompt_text = load_prompts("rag_summarize_prompt_path")
       self.prompt_template = PromptTemplate.from_template(self.prompt_text)
       self.model = chat_model
       self.chain = self._init_chain()

    def get_prompts(self, prompts):
        print("="*30)
        print(prompts)
        print("=" * 30)
        return prompts

    def _init_chain(self):
       chain = self.prompt_template | self.get_prompts | self.model | StrOutputParser()
       return chain

    def retriver_doc(self, query) -> list[Document]:
       return self.retriver.invoke(query)

    def rag_summarize(self, question):
       content = ''
       counter = 0
       documtnts :list[Document] = self.retriver_doc(question)
       for document in documtnts:
          counter += 1
          content += f'参考文档{counter}, 参考内容:{document.page_content}\n'

       return self.chain.invoke({
          "input":question,
          "context":content
       })

if __name__ == '__main__':
    rag = RagSummarizeService()
    print(rag.rag_summarize("小户型适合什么扫地机器人"))
