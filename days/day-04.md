# Day 4 - LangChain 深度：Chains 与高级 Agents

**日期**: 2026-04-01（周三）  
**预计时间**: 5-6 小时  
**难度**: ⭐⭐⭐⭐

---

## 📚 学习目标

1. 深入理解 LangChain Chains
2. 掌握多种 Agent 类型
3. 学习多步骤任务处理
4. 构建复杂工作流

---

## 📖 学习内容

### 上午（2.5 小时）

#### 1. Chains 深入（1 小时）
- [ ] SequentialChain
- [ ] TransformChain
- [ ] RouterChain
- [ ] 自定义 Chain

#### 2. Agent 类型对比（1.5 小时）
- [ ] Zero-shot React
- [ ] Structured Chat Agent
- [ ] OpenAI Functions Agent
- [ ] Plan-and-Execute Agent

### 下午（2.5-3.5 小时）

#### 3. 多步骤任务处理（1.5 小时）
- [ ] 任务分解
- [ ] 子任务调度
- [ ] 结果聚合

#### 4. 实践：多步骤 Agent（1-2 小时）
创建一个能处理复杂任务的 Agent：
- [ ] 接收复杂指令
- [ ] 自动分解任务
- [ ] 按顺序执行
- [ ] 汇总结果

---

## 💻 代码任务

### 任务：多步骤研究助手

```python
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 定义多个工具
tools = [
    Tool(name="Search", func=search_tool, description="搜索信息"),
    Tool(name="Calculator", func=calc_tool, description="计算"),
    Tool(name="Note", func=note_tool, description="记录笔记"),
]

# 使用更强大的 Agent 类型
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 测试复杂任务
response = agent.run(
    "帮我研究一下 AI Agent 的发展趋势，"
    "先搜索最新信息，然后总结关键点，"
    "最后计算一下市场规模增长率"
)
```

---

## ✅ 完成检查

- [ ] 理解不同 Chain 类型
- [ ] 掌握 3 种以上 Agent 类型
- [ ] 能处理多步骤任务
- [ ] 代码提交到 Git

---

## 📝 笔记区域

---

## 🔗 资源链接

- [LangChain Chains 文档](https://python.langchain.com/docs/modules/chains/)
- [Agent 类型对比](https://python.langchain.com/docs/modules/agents/agent_types/)
