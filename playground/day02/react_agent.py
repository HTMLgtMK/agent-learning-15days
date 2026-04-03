#!/usr/bin/env python3

"""
Agent 练习：LLM + TOOLS， ReAct 设计模式
"""

from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage, AIMessageChunk
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain_core.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchResults

from dotenv import load_dotenv
import os

# 加载环境变量
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

llm = ChatOpenAI(
    model="MiniMax-M2.7",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL"),
    temperature=0.7
)

def prompt_template():
    resp: AIMessage = llm.invoke([
        SystemMessage(content="你是我的人工智能助手，帮助我解答问题。"),
        HumanMessage(content="你好！")
    ])

    print("AI 回复：", resp.content)

    print('\n', '*' * 50)

    for chunk in llm.stream([HumanMessage(content="讲个笑话")]):
        print(chunk.content, end="", flush=True)
        pass

    print('\n', '*' * 50)

    template = PromptTemplate(template="你好，帮我查询{city}的天气", input_variables=['city'])
    prompt = template.format(city="长沙")
    print(llm.invoke(prompt).content)

    print('\n', '*' * 50)
    pass

def agent_with_tools():
    def search(query: str) -> str:
        """搜索工具，模拟搜索引擎查询"""
        result = DuckDuckGoSearchRun().run(query)
        return f"搜索结果：{result}"

    def calculator(expression: str) -> str:
        """计算器工具，计算简单的数学表达式"""
        return f"计算结果：{eval(expression)}"

    search_tool = Tool(
        name="Search",
        func=search,
        description="一个搜索工具，可以用来查询各种信息。输入一个查询字符串，返回搜索结果。",
    )

    calculator_tool = Tool(
        name="Calculator",
        func=calculator,
        description="一个计算工具，可以用来计算简单的数学表达式。输入一个数学表达式，返回计算结果。",
    )

    graph = create_agent(llm, tools=[search_tool, calculator_tool], name="MyAgent", system_prompt="你是一个智能助手，可以使用搜索工具和计算工具来回答用户的问题。", debug=False)

    input = {
        "messages": [HumanMessage(content="请帮我查询一下2024年奥运会的举办城市，并计算一下2024-2020的结果。")]
    }
    for chunk in graph.stream(input=input, stream_mode="messages"):
        msg, metadata = chunk  # stream_mode="messages" 返回 (message, metadata) 元组

        if isinstance(msg, AIMessageChunk):
            node = metadata.get("langgraph_node", "model")
            content = msg.content
            if content:  # 只打印有内容的消息
                print(f"[{node}] AI: {content}", flush=True)
        elif isinstance(msg, ToolMessage):
            node = metadata.get("langgraph_node", "tools")
            print(f"[{node}] Tool: {msg.name} -> {msg.content}", flush=True)
        elif hasattr(msg, 'content') and msg.content:
            print(f"[{metadata.get('langgraph_node', '?')}] {msg.type}: {msg.content}", flush=True)
    
    print('\n', '*' * 50)
    pass


if __name__ == "__main__":
    # prompt_template()
    agent_with_tools()
    pass