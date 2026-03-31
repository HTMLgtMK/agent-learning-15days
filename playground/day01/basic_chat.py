#!/usr/bin/env python3
"""
Day 1: 第一个 LLM 对话
学习目标：理解 API 调用基本流程
"""

from openai import OpenAI
from dotenv import load_dotenv
import os


# 加载环境变量
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

# 初始化客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL")
)


def create_personal_assistant():
    """创建一个个人助理"""
    response = client.chat.completions.create(
        model="MiniMax-M2.7",
        messages=[
            {"role": "system", "content": "你是 GBoss 的个人助手，了解以下信息：\n- 姓名：GBoss\n- 职业：安卓开发工程师\n- 目标：转行 AI Agent 开发\n- 地点：广州"},
            {"role": "user", "content": "请介绍一下你自己。"}
        ],
        temperature=0.7,
        max_tokens=200
    )
    print("AI 回复：", response.choices[0].message.content)
    print("token usage:", response.usage.total_tokens)
    pass


def main():
    """与 LLM 进行简单对话"""
    response = client.chat.completions.create(
        model="MiniMax-M2.7",
        messages=[
            {"role": "system", "content": "你是我的人工智能助手，帮助我解答问题。"},
            {"role": "user", "content": "你好！你能介绍一下自己吗？用的什么模型？"}
        ],
        temperature=0.7,
        max_tokens=200
    )
    print("AI 回复：", response.choices[0].message.content)
    print("token usage:", response.usage.total_tokens)

    pass


if __name__ == "__main__":
    main()
    print("*" * 50)
    create_personal_assistant()
    pass

