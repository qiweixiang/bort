import random

from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain_core.tools import tool
from agent.rag.RagSummarizeService import RagSummarizeService
from agent.utils.config_handler import agent_yml
from agent.utils.file_handler import get_abs_path
from agent.utils.logger_handler import logger



rag = RagSummarizeService()
user_ids = ["1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010",]
month_arr = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06",
             "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12", ]

external_data = {}

@tool(description="从向量存储中检索参考资料")
def rag_summarize(question):
    print("rag_summarize:")
    return rag.rag_summarize(question)

@tool(description="获取指定城市的天气信息，以字符串的形式返回")
def get_weather(city):
    return f"城市{city}天气为晴天，气温26摄氏度，空气湿度50%，南风一级，AQI21,最近六小时降雨概率极低"


@tool(description="获取用户所在城市名称，以字符串返回")
def get_user_location():
    return "上海"


@tool(description="获取用户ID，以字符串返回")
def get_user_id():
    return random.choice(user_ids)

@tool(description="获取当前月份，以字符串返回")
def get_current_month():
    return random.choice(month_arr)

def get_external_data(user_id :str):
    """
        {
            user_id :{
                month:{},
                month:{}
            },
            user_id :{
                month:{},
                month:{}
            }
        }

    :param user_id:
    :param month:
    :return:
    """
    if external_data:
        return external_data[user_id]
    external_data_path = get_abs_path(agent_yml['external_data_path'])
    with open(external_data_path, "r", encoding="utf-8") as f:
       for line in f.readlines()[1:]:
            line = line.strip()
            arr_list = line.split(",")
            #"用户ID","特征","清洁效率","耗材","对比","时间"
            user_id_inner = arr_list[0].replace('"', '')
            feature = arr_list[1].replace('"', '')
            clean_efficiency = arr_list[2].replace('"', '')
            material = arr_list[3].replace('"', '')
            compare = arr_list[4].replace('"', '')
            month = arr_list[5].replace('"', '')
            if user_id_inner not in external_data:
                external_data[user_id_inner] = {}

            external_data[user_id_inner][month] = {
                "feature":feature,
                "clean_efficiency":clean_efficiency,
                "material":material,
                "compare":compare
            }

@tool(description="从外部系统中获取用户指定月份的使用，返回字符串")
def fetch_external_data(user_id :str, month :str):
    get_external_data(user_id)
    try:
        return external_data[user_id][month]
    except KeyError as e:
        logger.error(f"fetch_external_data,未查询到用户{user_id}{month}月份的使用记录")
        return ""

@tool(description="无入参，无返回值，调用后触发中间件自动为报告生成的场景动态注入上下文信息，为后续提示词切换提供上下文信息")
def fill_context_for_report():
    return "fill_context_for_report已调用"



if __name__ == '__main__':
    print(fetch_external_data("1001", "2025-01"))
