from agent.utils.config_handler import prompts_yml
from agent.utils.logger_handler import logger
from agent.utils.path_tool import get_abs_path


def load_prompts(key):
    try:
        full_path = get_abs_path(prompts_yml[key])
    except KeyError as e:
        logger.error(f"加载提示词异常:{key}")
        raise e

    try:
        return open(full_path, encoding="utf-8").read()
    except Exception as e:
        logger.error(f"加载提示词异常:{key}")
        raise e

if __name__ == '__main__':
    # print(load_prompts("main_prompt_path"))
    print(load_prompts("rag_summarize_prompt_path"))