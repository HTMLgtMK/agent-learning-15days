# Day 9 - 工具开发：自定义 Tools 与 API 集成

**日期**: 2026-04-06（周一）  
**预计时间**: 5-6 小时  
**难度**: ⭐⭐⭐⭐

---

## 📚 学习目标

1. 掌握自定义 Tool 开发
2. 学习 API 集成方法
3. 理解 Tool 设计规范
4. 为 Agent 添加 3-5 个自定义工具

---

## 📖 学习内容

### 上午（2.5 小时）

#### 1. Tool 设计原则（1 小时）
- [ ] Tool 命名规范
- [ ] 参数设计
- [ ] 返回值格式
- [ ] 错误处理
- [ ] 描述编写（影响 Agent 理解）

#### 2. LangChain Tool 类型（1.5 小时）
- [ ] Function Tool
- [ ] Structured Tool
- [ ] API Tool
- [ ] 自定义 Tool 类

### 下午（2.5-3.5 小时）

#### 3. 实践：开发自定义工具（2 小时）
为个人助手添加新工具：
- [ ] 笔记管理工具
- [ ] 文件操作工具
- [ ] 网络请求工具
- [ ] 数据库工具

#### 4. API 集成（30 分钟）
- [ ] REST API 调用
- [ ] 认证处理
- [ ] 速率限制
- [ ] 缓存策略

---

## 💻 代码任务

### 任务 1: 自定义工具类

```python
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class NoteInput(BaseModel):
    title: str = Field(description="笔记标题")
    content: str = Field(description="笔记内容")

class NoteTool(BaseTool):
    name = "note_manager"
    description = "用于创建、查询、管理笔记"
    args_schema: Type[BaseModel] = NoteInput
    
    def _run(self, title: str, content: str) -> str:
        # 实现笔记保存逻辑
        save_note(title, content)
        return f"笔记 '{title}' 已保存"
    
    async def _arun(self, title: str, content: str) -> str:
        # 异步实现
        return self._run(title, content)
```

### 任务 2: API 集成工具

```python
from langchain.tools import tool
import requests

@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气"""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.weather.com/{city}"
    response = requests.get(url, params={"key": api_key})
    return parse_weather(response.json())
```

---

## ✅ 完成检查

- [ ] 理解 Tool 设计原则
- [ ] 开发 3+ 自定义工具
- [ ] 完成 API 集成
- [ ] 工具能被 Agent 正确调用
- [ ] 代码提交到 Git

---

## 📝 笔记区域

---

## 🔗 资源链接

- [LangChain Tools 文档](https://python.langchain.com/docs/modules/agents/tools/)
- [自定义 Tools 教程](https://python.langchain.com/docs/modules/agents/how_to/custom_tools)
