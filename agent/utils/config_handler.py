import yaml
from agent.utils.path_tool import get_abs_path

def load_config(config_path :str, encoding :str = "utf-8"):
    with open(get_abs_path(config_path), encoding=encoding, mode="r") as f:
        # 使用yaml直接加载整个文件
        return yaml.load( f, Loader=yaml.FullLoader)

agent_yml = load_config("config/agent.yml")
chroma_yml = load_config("config/chroma.yml")
prompts_yml = load_config("config/prompts.yml")
rag_yml = load_config("config/rag.yml")


if __name__ == '__main__':
    print(agent_yml['chat_model_name'])