# Day 6 - 多 Agent 框架对比：AutoGen 与 CrewAI

**日期**: 2026-04-03（周五）  
**预计时间**: 5-6 小时  
**难度**: ⭐⭐⭐⭐

---

## 📚 学习目标

1. 了解 AutoGen 框架
2. 掌握 CrewAI 使用
3. 对比不同框架的优劣
4. 实现多 Agent 团队

---

## 📖 学习内容

### 上午（2.5 小时）

#### 1. AutoGen 基础（1.5 小时）
- [ ] AutoGen 核心概念
- [ ] ConversableAgent
- [ ] 群聊模式
- [ ] 代码执行能力

#### 2. CrewAI 基础（1 小时）
- [ ] CrewAI 设计理念
- [ ] Agent 角色定义
- [ ] Task 与 Process
- [ ] Crew 编排

### 下午（2.5-3.5 小时）

#### 3. 实践：CrewAI 多 Agent 团队（2 小时）
创建一个多角色团队：
- [ ] 定义研究员 Agent
- [ ] 定义作家 Agent
- [ ] 定义编辑 Agent
- [ ] 编排协作流程

#### 4. 框架对比总结（30 分钟）
- [ ] LangChain vs AutoGen vs CrewAI
- [ ] 各自适用场景
- [ ] 选择建议

---

## 💻 代码任务

### 任务：CrewAI 内容创作团队

```python
from crewai import Agent, Task, Crew, Process

# 定义角色
researcher = Agent(
    role='高级研究员',
    goal='深入调研主题，收集关键信息',
    backstory='你是一位经验丰富的研究员，擅长从海量信息中提取关键洞察',
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role='资深作家',
    goal='根据研究结果撰写高质量文章',
    backstory='你是一位获奖作家，擅长将复杂信息转化为易懂的文章',
    verbose=True,
    allow_delegation=False
)

# 定义任务
research_task = Task(
    description='调研 AI Agent 的最新发展趋势',
    agent=researcher,
    expected_output='一份详细的研究大纲'
)

write_task = Task(
    description='根据研究结果撰写一篇 2000 字的文章',
    agent=writer,
    expected_output='一篇完整的文章'
)

# 组建团队
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

# 执行
result = crew.kickoff()
```

---

## ✅ 完成检查

- [ ] 理解 AutoGen 基础
- [ ] 掌握 CrewAI 使用
- [ ] 完成多 Agent 团队示例
- [ ] 能对比不同框架
- [ ] 代码提交到 Git

---

## 📝 笔记区域

---

## 🔗 资源链接

- [AutoGen 文档](https://microsoft.github.io/autogen/)
- [CrewAI 文档](https://docs.crewai.com/)
- [框架对比文章](https://blog.langchain.dev/agent-framework-comparison/)
