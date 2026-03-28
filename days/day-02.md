# Day 2 - Agent 核心概念与 LangChain 入门

**日期**: 2026-03-30（周一）  
**预计时间**: 4-5 小时  
**难度**: ⭐⭐⭐

---

## 📚 学习目标

1. 理解 AI Agent 的核心概念
2. 掌握 ReAct 设计模式
3. 学习 LangChain 基础
4. 创建第一个带工具调用的 Agent

---

## 📖 学习内容

### 上午（2 小时）

#### 1. Agent 核心概念（45 分钟）
- [ ] 什么是 AI Agent？
- [ ] Agent vs 普通 LLM 调用
- [ ] ReAct 模式（Reason + Act）
- [ ] Tool Use（工具使用）
- [ ] Agent 的工作流程

#### 2. 阅读材料
- [ ] [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [ ] [LangChain Agent 文档](https://python.langchain.com/docs/modules/agents/)

### 下午（2-3 小时）

#### 3. LangChain 基础（1 小时）
```bash
# 安装 LangChain
pip install langchain langchain-openai langchain-community
```

学习核心概念：
- [ ] LLM 封装
- [ ] Prompt Templates
- [ ] Chains
- [ ] Tools

#### 4. 第一个 Agent（1.5 小时）
创建一个能使用工具的 Agent：
- [ ] 使用内置工具（搜索、计算器）
- [ ] 理解 AgentExecutor
- [ ] 测试工具调用流程

---

## 💻 代码任务

创建文件 `day-02/agent_with_tools.py`:

```python
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

# 初始化搜索工具
search = DuckDuckGoSearchRun()
tools = [Tool(
    name="Search",
    func=search.run,
    description="用于搜索互联网获取最新信息"
)]

# 初始化 LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 创建 Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 测试
response = agent.run("今天北京的天气怎么样？")
print(response)
```

---

## ✅ 完成检查

- [ ] 理解 Agent 与普通 LLM 调用的区别
- [ ] 掌握 ReAct 模式原理
- [ ] 成功运行 LangChain Agent
- [ ] Agent 能正确调用工具
- [ ] 代码提交到 Git

---

## 📝 笔记区域

（学习完成后在此记录笔记和心得）

---

## 🔗 资源链接

- [LangChain 官方文档](https://python.langchain.com/docs/get_started/introduction)
- [LangChain Agents 详解](https://python.langchain.com/docs/modules/agents/)
- [ReAct 论文解读](https://lilianweng.github.io/posts/2023-05-07-agentic-llm/)
