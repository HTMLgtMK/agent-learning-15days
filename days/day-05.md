# Day 5 - LangGraph：状态机与工作流

**日期**: 2026-04-02（周四）  
**预计时间**: 5-6 小时  
**难度**: ⭐⭐⭐⭐⭐

---

## 📚 学习目标

1. 理解 LangGraph 核心概念
2. 掌握状态机设计
3. 学习多 Agent 协作
4. 构建有状态的工作流

---

## 📖 学习内容

### 上午（2.5 小时）

#### 1. LangGraph 基础（1.5 小时）
- [ ] 什么是 LangGraph？
- [ ] State（状态）概念
- [ ] Node（节点）定义
- [ ] Edge（边）与条件路由

#### 2. 状态机设计（1 小时）
- [ ] 有限状态机原理
- [ ] 在 Agent 中的应用
- [ ] 状态转换逻辑

### 下午（2.5-3.5 小时）

#### 3. 构建工作流（1.5 小时）
- [ ] 定义 State Schema
- [ ] 创建 Nodes
- [ ] 添加 Edges
- [ ] 编译并运行 Graph

#### 4. 多 Agent 协作（1-2 小时）
- [ ] 多角色设计
- [ ] 任务分发
- [ ] 结果汇总

---

## 💻 代码任务

### 任务：内容创作工作流

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# 定义状态
class State(TypedDict):
    topic: str
    outline: str
    draft: str
    final: str
    messages: Annotated[list, operator.add]

# 创建节点
def researcher(state):
    # 研究主题
    return {"outline": "研究结果..."}

def writer(state):
    # 撰写草稿
    return {"draft": "草稿内容..."}

def editor(state):
    # 编辑润色
    return {"final": "最终版本..."}

# 构建图
workflow = StateGraph(State)
workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)
workflow.add_node("editor", editor)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "editor")
workflow.add_edge("editor", END)

app = workflow.compile()

# 运行
result = app.invoke({"topic": "AI Agent 发展趋势", "messages": []})
```

---

## ✅ 完成检查

- [ ] 理解 LangGraph 核心概念
- [ ] 能定义 State 和 Nodes
- [ ] 实现条件路由
- [ ] 完成工作流示例
- [ ] 代码提交到 Git

---

## 📝 笔记区域

---

## 🔗 资源链接

- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- [LangGraph 教程](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
