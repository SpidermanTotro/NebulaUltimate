# Nebula Ultimate: Copilot & AI Family — Skills Manifest

This document catalogs the default and recommended skills of Copilot (and related agents) in Nebula Ultimate.  
All skills are open, modifiable, and free of enforced restrictions.  
You can add, update, or remove any skill by editing or dropping `.py` files in `/ai_agents/`.

---

## 🧠 Core Copilot Skills

| Skill                        | File/Agent           | Description                                                                     | Limits?     |
|------------------------------|----------------------|---------------------------------------------------------------------------------|-------------|
| Code Generation              | copilot.py           | Generate code/functions/classes from prompts and specs.                         | None        |
| Code Completion              | copilot.py           | Autocomplete code snippets or partial code.                                     | None        |
| Code Explanation             | copilot.py           | Explain code in natural language.                                               | None        |
| Code Review & Bug Spotting   | bugfinder.py         | Analyze and critique code, detect bugs and anti-patterns.                       | None        |
| Test Generation              | copilot.py           | Generate unit, integration, or property-based tests for code.                   | None        |
| Docstring/Comment Generation | docgen.py            | Generate Pythonic/JS/Javadoc/Rustdoc-style docstrings and inline comments.      | None        |
| Refactoring                  | copilot.py           | Suggest or apply improvements for clarity, speed, readability, or patterns.     | None        |
| Code Translation             | translator.py        | Convert code from one programming language to another.                          | None        |
| Pattern Detection            | bugfinder.py         | Recognize good/bad practices in code structures or approaches.                  | None        |
| Q&A / Dev-Assistant Chat     | copilot.py, chatgpt.py| Answer questions about coding, dev workflows, algorithms, and tooling.           | None        |
| Design Helper                | designhelper.py      | Analyze or suggest UI/UX, asset layouts, or GUI controls from code.             | None        |
| Code Optimizer/Advisor       | optimizer.py         | Advise on speed, memory use, idioms, or optimize code for a given metric.       | None        |

---

## 🧩 Extensibility & Community Skills

- **Add new .py skills**: Any Python file with a `respond(prompt)` function in `/ai_agents/` becomes instantly available.
- **Fork or upload new agents**: UI and API provided for skill sharing, ranking, and install/removal.
- **No moderation, scripting, or company lock-in by default**—restrictions are what you choose to set, not what’s imposed.

---

## 🌟 Example AI Skill Extensions

- **Image-to-code** (`img2code.py`): Extracts code from screenshots or diagrams.
- **Auto-migrate** (`migrator.py`): Refactors legacy codebases to modern language standards.
- **Security Audit** (`security.py`): Looks for known vulnerabilities and auto-patches.
- **Voice-to-Code** (`voicecode.py`): Lets you drive Copilot with speech.

---

## 💻 Contribution & Growth

- Every skill is open, reviewable, and forkable.
- Contributors may submit any kind of agent: creative, utility, research, or fun.
- Marketplace/community system helps discover and improve the ecosystem.
- “Super AI” workflows (chaining, ensemble, debate modes) are supported.

---

## 🔗 See Also

- [Developer Guidelines](./dev_guidelines.md)
- [Architecture](./architecture.md)
- [Onboarding](./onboard.md)

---

**You are free to update this file and these skills anytime—  
Nebula Ultimate’s AI family grows as you and your collaborators dream.**