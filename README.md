<div align="center">

# 📚 书灵.skill · Shuling

**把一本书、一门课、一套资料，蒸馏成可调用的 AI 顾问**

[![GitHub stars](https://img.shields.io/github/stars/AnonymousLeeJJ/shuling-skill?style=social)](https://github.com/AnonymousLeeJJ/shuling-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[English](README_EN.md) ｜ [示例顾问](examples/) ｜ [贡献指南](CONTRIBUTING.md)

</div>

---

## 🤔 这是什么？

书架上读完的书，大部分都忘了吧？

书灵把**知识源**（书 / 课程 / 文档 / 系列文章）蒸馏成一个**符合 Agent Skills 规范的顾问 skill**。装好之后，这本书就变成了一个随叫随到的顾问：

> 💬 「用《金字塔原理》的顾问，帮我改这篇项目汇报。」
> 💬 「让《非暴力沟通》的顾问，看看我跟同事这段对话哪里有问题。」
> 💬 「用《原则》的顾问，帮我复盘这次决策。」

**它不是「回答关于这本书的问题」，而是「用这本书的方法论解决你的问题」。**

## ✨ 蒸馏流程（四阶段）

```
摄入资料 → 拆解知识框架 → 提炼顾问内核 → 质量验证
```

| 阶段 | 做什么 | 关键标准 |
| --- | --- | --- |
| 0 摄入 | 确认资料形态和你的用途 | 没读过的书不臆造，先补资料 |
| 1 拆解 | 输出知识地图：核心问题、模块、主线逻辑 | 区分方法论骨架与案例血肉 |
| 2 提炼 | 方法论 3-7 条 + 工作流程 + 检查清单 + 常见误区 | 三重验证：有生成力、可操作、有辨识度 |
| 3 生成 | 产出标准 SKILL.md + references | 主文件 ≤400 行，细节入 references |
| 4 验证 | 一致性 / 生成力 / 谦逊度三项测试 | 不达标打回重做，附验证记录 |

## 🎯 示例：《金字塔原理》顾问

仓库里附了一个**完整蒸馏成品**：[examples/pyramid-principle](examples/pyramid-principle/SKILL.md)，包括：

- 7 条核心方法论（结论先行、MECE、SCQA……）
- 「改汇报」「从零起草」两条工作流程
- 7 条验收检查清单、5 个常见误区
- 精选案例库与蒸馏验证记录

装好后试试对它说：

> 「这是我写的季度汇报，帮我用金字塔原理改一改：……」

## 🚀 安装与使用

### Claude Code

```bash
# 安装书灵本体（蒸馏器）
mkdir -p ~/.claude/skills/shuling
cp SKILL.md ~/.claude/skills/shuling/SKILL.md

# 安装示例顾问
cp -r examples/pyramid-principle ~/.claude/skills/
```

然后对 Claude 说：「用 shuling 把《思考，快与慢》蒸馏成顾问。」

### WorkBuddy / 其他支持 Skills 的 Agent

把 `SKILL.md` 复制到对应 skills 目录即可（WorkBuddy 为 `~/.workbuddy/skills/shuling/`）。凡支持 Agent Skills 协议的工具均可使用。

### 蒸馏你自己的第一本书

1. 装好 shuling 后，对 Agent 说：「用书灵蒸馏《书名》，我打算用它来【你的用途】」
2. 按提示提供资料（电子书文本最佳，目录+读书笔记也可以）
3. 走完四阶段，得到 `distilled/<书名>/` 顾问文件夹
4. 复制到 skills 目录，开始咨询

## 📁 仓库结构

```
shuling-skill/
├── SKILL.md                      # 书灵本体：蒸馏流程与规范
├── templates/
│   └── advisor-template.md       # 顾问模板（蒸馏时生成用）
├── examples/
│   └── pyramid-principle/        # 示例：《金字塔原理》完整顾问
│       ├── SKILL.md
│       ├── references/           # 蒸馏稿 + 案例库
│       └── research/             # 质量验证记录
└── scripts/
    └── validate.py               # 顾问结构校验脚本
```

校验你蒸馏的顾问：

```bash
python scripts/validate.py distilled/your-book
```

## 🤝 贡献

- 欢迎提交你蒸馏的顾问（放 `examples/`，附 `research/validation.md` 验证记录）
- 欢迎改进蒸馏流程本身
- 详见 [贡献指南](CONTRIBUTING.md)

## 📄 许可

[MIT](LICENSE) —— 随意使用，包括商用。

---

<div align="center">

**如果这个项目对你有帮助，请点个 ⭐ Star 支持一下！**

</div>
