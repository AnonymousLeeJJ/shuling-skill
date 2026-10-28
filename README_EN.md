<div align="center">

# 📚 Shuling Skill

**Distill any book, course, or document set into a callable AI advisor**

[![GitHub stars](https://img.shields.io/github/stars/AnonymousLeeJJ/shuling-skill?style=social)](https://github.com/AnonymousLeeJJ/shuling-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[中文版](README.md) ｜ [Example Advisor](examples/)

</div>

---

## What is this?

Most books we read fade from memory. Shuling turns a **knowledge source** (book / course / docs / article series) into an **Agent Skills–compatible advisor skill**. Once installed, the book becomes an advisor you can consult anytime:

> "Using my Pyramid Principle advisor, help me rewrite this project report."
> "Let my Nonviolent Communication advisor review this conversation with my colleague."

**It doesn't answer questions *about* the book — it solves *your* problems *with* the book's methodology.**

## How it works

```
Ingest → Map the framework → Distill the advisor core → Validate
```

- **Ingest**: confirm source material and your intended use. Never fabricates content for unknown books.
- **Map**: core questions, module map, argument spine; separates methodology from anecdotes.
- **Distill**: 3–7 methodologies + workflows + acceptance checklist + common pitfalls. Every methodology must pass three tests: generative, actionable, distinctive.
- **Validate**: consistency / generativity / humility tests, with a written validation report.

## Example included

A complete advisor distilled from *The Pyramid Principle*: [examples/pyramid-principle](examples/pyramid-principle/SKILL.md) — 7 methodologies, 2 workflows, 7-point checklist, case library, validation record.

## Install (Claude Code)

```bash
mkdir -p ~/.claude/skills/shuling
cp SKILL.md ~/.claude/skills/shuling/SKILL.md
cp -r examples/pyramid-principle ~/.claude/skills/
```

Then say: "Use shuling to distill *Thinking, Fast and Slow* into an advisor."

Works with any agent supporting the Agent Skills protocol (Claude Code, Codex, Cursor, WorkBuddy, etc.).

## Validate your own distillations

```bash
python scripts/validate.py distilled/your-book
```

## License

[MIT](LICENSE)
