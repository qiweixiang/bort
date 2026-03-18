from langchain.agents.middleware import wrap_tool_call, before_model, dynamic_prompt, ModelRequest
from agent.utils.logger_handler import logger
from agent.utils.prompt_loader import load_prompts

@wrap_tool_call
def monitor_tool(request,
                 handler):
    logger.info(f"monitor_tool开始调用工具:{request.tool_call['name']}, 传入参数:{request.tool_call['args']}")
    try:
        result = handler(request)
        logger.info(f"monitor_tool调用工具:{request.tool_call['name']} 成功")

        if request.tool_call['name'] == 'fill_context_for_report':
            request.runtime.context['report'] = True
        return result
    except Exception as e:
        logger.error(f"monitor_tool调用工具:{request.tool_call['name']} 失败,错误信息:{str(e)}")
        raise e

@before_model
def log_before_model(state,
                     runtime):
    logger.info(f"log_before_model即将调用模型，参数{len(state['messages'])}条消息")

    return None


@dynamic_prompt
def report_prompt_switch(request :ModelRequest):
    """
    动态切换提示词的功能
    :param request:
    :return:
    """
    is_report = request.runtime.context.get('report', False)
    if is_report:
        return load_prompts('report_prompt_path')
    return load_prompts('main_prompt_path')


