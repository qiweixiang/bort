from langchain.agents import create_agent
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool


# @tool(description="查询天气")
# def get_weather() -> str:
#     return "下雨"
#
# agent = create_agent(
#     model=ChatTongyi(model="qwen-max"),
#     tools=[get_weather],
#     system_prompt="你是一个聊天助手负责回答用户问题"
# )
# res = agent.invoke(
#     {
#         "messages":[
#             {"role":"user", "content":"明天北京的天气怎么样"}
#         ]
#     }
# )
#
# for message in res['messages']:
#     print(type(message).__name__, message.content)


# @tool(description="获取股票信息，传入股票，返回字符串信息")
# def get_info(name) -> str:
#     return f"股票{name}是一个上市公司，专注于IT教育服务"
#
#
# @tool(description="获取股票价格信息，传入股票，返回价格")
# def get_price(name) -> str:
#     return f"股票{name}的股价是20元"
#
#
# agent = create_agent(
#     model=ChatTongyi(model="qwen-max"),
#     tools=[get_info, get_price],
#     system_prompt="你是一个聊天助手负责回答用户问题"
# )
# for chunk in agent.stream(
#     {
#         "messages":[
#             {"role":"user", "content":"传智播客的股价是多少，并介绍一下"}
#         ]
#     },
#     stream_mode="values"
# ):
#     last_msg = chunk['messages'][-1]
#     if last_msg.content:
#         print(type(last_msg).__name__, last_msg.content)


# @tool(description="获取身高信息，返回的是厘米")
# def get_height():
#     return 181
#
#
# @tool(description="获取体重信息，返回的是kg")
# def get_weight():
#     return 74
#
#
# agent = create_agent(
#     model=ChatTongyi(model="qwen-max"),
#     tools=[get_height, get_weight],
#     system_prompt="""你是严格遵循ReAct框架的智能体，必须按「思考→行动→观察→再思考」的流程解决问题，、
#     并告知我你的思考过程以及调用工具的名称，工具的调用原因、名称，按思考、行动、观察三个结构告知我，【并且把每个过程通过文字标注一下】""",
# )
# for chunk in agent.stream(
#     {
#         "messages":[
#             {"role":"user", "content":"我想计算一下我的BMI"}
#         ]
#     },
#     stream_mode="values"
# ):
#     last_msg = chunk['messages'][-1]
#     if last_msg.content:
#         print(type(last_msg).__name__, last_msg.content)


@tool(description="查询天气")
def get_weather(city) -> str:
    return "下雨"

@before_agent
def before_agent_invoke(state, runtime):
    print("before_agent_invoke")

@after_agent
def after_agent_invoke(state, runtime):
    print("after_agent_invoke")

@before_model
def before_model_invoke(state, runtime):
    print("before_model_invoke")

@after_model
def after_model_invoke(state, runtime):
    print("after_model_invoke")

agent = create_agent(
    model=ChatTongyi(model="qwen-max"),
    tools=[get_weather],
    middleware=[before_agent_invoke, after_agent_invoke, before_model_invoke, after_model_invoke],
    system_prompt="你是一个聊天助手负责回答用户问题"
)
res = agent.invoke(
    {
        "messages":[
            {"role":"user", "content":"明天北京的天气怎么样"}
        ]
    }
)

for message in res['messages']:
    print(type(message).__name__, message.content)
