# Day 3 - 记忆系统与 RAG 基础

**日期**: 2026-03-31（周二）  
**预计时间**: 4-5 小时  
**难度**: ⭐⭐⭐

---

## 📚 学习目标

1. 理解 Agent 记忆系统
2. 掌握对话历史管理
3. 学习 RAG（检索增强生成）基础
4. 实现带记忆的对话助手

---

## 📖 学习内容

### 上午（2 小时）

#### 1. 记忆系统（1 小时）
- [ ] 为什么 Agent 需要记忆？
- [ ] 短期记忆 vs 长期记忆
- [ ] ConversationBufferMemory
- [ ] ConversationSummaryMemory
- [ ] 记忆窗口管理

#### 2. RAG 基础（1 小时）
- [ ] 什么是 RAG？
- [ ] Vector Database 原理
- [ ] Embedding 基础
- [ ] 检索与生成流程

### 下午（2-3 小时）

#### 3. 实现对话记忆（1 小时）
- [ ] 使用 LangChain Memory
- [ ] 实现多轮对话
- [ ] 测试记忆效果

#### 4. RAG 实践（1.5 小时）
- [ ] 安装 ChromaDB
- [ ] 创建文档索引
- [ ] 实现基于文档的问答

---

## 💻 代码任务

### 任务 1: 带记忆的对话机器人

```python
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# 多轮对话测试
conversation.predict(input="你好，我叫 GBoss")
conversation.predict(input="我刚才告诉你什么名字？")
```

### 任务 2: 简单的 RAG 问答

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# 准备文档
texts = ["你的文档内容..."]

# 创建向量存储
embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.create_documents(texts)

# 存储到 Chroma
db = Chroma.from_documents(docs, embeddings)

# 检索
results = db.similarity_search("你的问题")
```

---

## ✅ 完成检查

- [ ] 理解记忆系统的作用
- [ ] 实现多轮对话
- [ ] 理解 RAG 原理
- [ ] 完成简单的文档问答
- [ ] 代码提交到 Git

---

## 📝 笔记区域

---

## 🔗 资源链接

- [LangChain Memory 文档](https://python.langchain.com/docs/modules/memory/)
- [RAG 详解](https://lilianweng.github.io/posts/2023-12-21-agentic-llm-part-2/)
- [ChromaDB 文档](https://docs.trychroma.com/)
