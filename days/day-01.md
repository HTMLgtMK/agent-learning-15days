# Day 1 - LLM 基础与环境搭建

**日期**: 2026-03-29（周日）  
**预计时间**: 4-5 小时  
**难度**: ⭐⭐

---

## 📚 学习目标

1. 理解 LLM（大语言模型）的基本工作原理
2. 掌握 Prompt Engineering 基础技巧
3. 搭建 Python 开发环境
4. 完成第一个 API 调用

---

## 📖 学习内容

### 上午（2 小时）

#### 1. LLM 基础概念（30 分钟）
- [ ] 什么是 LLM？
- [ ] Token 是什么？如何计算？
- [ ] 上下文窗口（Context Window）
- [ ] Temperature、Top-P 等参数含义

#### 2. Prompt Engineering 基础（1 小时）
- [ ] Zero-shot vs Few-shot Prompting
- [ ] Chain of Thought（思维链）
- [ ] Role Prompting（角色设定）
- [ ] System Message vs User Message

#### 3. 阅读材料
- [ ] [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [ ] [LLM University - Cohere](https://docs.cohere.com/docs/llmu)

### 下午（2-3 小时）

#### 4. 环境搭建（1 小时）
```bash
# 创建项目目录
mkdir -p ~/ai-agent-learning && cd ~/ai-agent-learning

# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装基础依赖
pip install openai anthropic requests python-dotenv
```

#### 5. 第一个 API 调用（1 小时）
- [ ] 获取 API Key（OpenAI 或 国内替代）
- [ ] 编写第一个对话脚本
- [ ] 测试不同参数的效果

#### 6. 实践任务（30 分钟）
创建一个简单的问答机器人，要求：
- 能回答关于你自己的问题
- 使用 System Message 设定角色
- 尝试不同的 Temperature 值观察输出差异

---

## 💻 代码任务

创建文件 `day-01/basic_chat.py`:

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个友好的助手。"},
        {"role": "user", "content": "你好，请介绍一下你自己。"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

---

## ✅ 完成检查

- [ ] 理解 LLM 基本概念
- [ ] 掌握 3 种以上 Prompt 技巧
- [ ] 环境搭建完成
- [ ] 成功调用 API 并获得响应
- [ ] 代码提交到 Git

---

## 📝 笔记区域

（学习完成后在此记录笔记和心得）

---

## 🔗 资源链接

- [OpenAI API 文档](https://platform.openai.com/docs)
- [Anthropic API 文档](https://docs.anthropic.com/claude/reference)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
