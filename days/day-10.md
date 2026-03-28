# Day 10 - LLM 原理深入：Token、参数与优化

**日期**: 2026-04-07（周二）  
**预计时间**: 5-6 小时  
**难度**: ⭐⭐⭐⭐

---

## 📚 学习目标

1. 深入理解 LLM 工作原理
2. 掌握关键参数调优
3. 学习成本与性能优化
4. 能根据场景选择合适的模型

---

## 📖 学习内容

### 上午（2.5 小时）

#### 1. Token 与上下文（1 小时）
- [ ] Token 计算原理
- [ ] 上下文窗口限制
- [ ] Token 成本计算
- [ ] 长文本处理策略

#### 2. 生成参数详解（1.5 小时）
- [ ] Temperature（随机性）
- [ ] Top-P（核采样）
- [ ] Top-K
- [ ] Frequency Penalty
- [ ] Presence Penalty
- [ ] 参数组合效果

### 下午（2.5-3.5 小时）

#### 3. 实验：参数对比（2 小时）
对同一 prompt 测试不同参数组合：
- [ ] Temperature: 0, 0.5, 0.7, 1.0
- [ ] Top-P: 0.8, 0.9, 1.0
- [ ] 记录输出差异
- [ ] 总结最佳实践

#### 4. 模型选择指南（30 分钟）
- [ ] GPT-4 vs GPT-3.5 vs Claude
- [ ] 本地模型（Llama、Qwen）
- [ ] 成本 vs 性能权衡
- [ ] 场景匹配建议

---

## 💻 代码任务

### 任务：参数对比实验

```python
import openai
import json

prompts = [
    "写一首关于 AI 的诗",
    "解释量子计算",
    "给我 5 个创业点子"
]

configs = [
    {"temperature": 0, "top_p": 1},
    {"temperature": 0.5, "top_p": 0.9},
    {"temperature": 0.7, "top_p": 0.9},
    {"temperature": 1.0, "top_p": 1}
]

results = []
for prompt in prompts:
    for config in configs:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            **config
        )
        results.append({
            "prompt": prompt,
            "config": config,
            "output": response.choices[0].message.content,
            "tokens": response.usage
        })

# 保存结果用于分析
with open("parameter_comparison.json", "w") as f:
    json.dump(results, f, indent=2)
```

---

## ✅ 完成检查

- [ ] 理解 Token 计算
- [ ] 掌握各参数作用
- [ ] 完成参数对比实验
- [ ] 能根据场景选择参数
- [ ] 代码提交到 Git

---

## 📝 笔记区域

---

## 🔗 资源链接

- [OpenAI API 参考](https://platform.openai.com/docs/api-reference)
- [LLM 参数详解](https://lilianweng.github.io/posts/2023-05-07-agentic-llm/)
