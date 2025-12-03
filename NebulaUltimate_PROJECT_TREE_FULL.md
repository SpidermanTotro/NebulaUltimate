NebulaUltimate/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── /nebula
│   ├── __init__.py
│   ├── app.py
│   ├── ai_hub.py
│   ├── plugin_manager.py
│   ├── /ui
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── panels.py           # For future asset/gallery/explorer, AI chat
│   │   ├── agent_marketplace.py# UI for downloading/enabling/disabling agents
│   │   └── onboarding.py       # Wizard/onboarding flow
│   ├── project_manager.py      # Project loading/saving
│   ├── file_explorer.py        # GUI file tree/explorer
│   ├── build_system.py         # Build/run orchestration
│   ├── test_runner.py          # Hook/execute tests
│   ├── doc_system.py           # Docs, markdown, onboarding integration
│   └── marketplace.py          # (plugin/AI skill store, community hub)
├── /ai_agents
│   ├── README.md
│   ├── copilot.py
│   ├── copilot_agent.py
│   ├── bugfinder.py
│   ├── chatgpt.py
│   ├── converter.py
│   ├── docgen.py
│   ├── designhelper.py         # (AI code → UI/UX convertor skill)
│   ├── optimizer.py            # (AI code optimization skill)
│   └── translator.py
├── /models
│   ├── ollama/
│   ├── starcoder/
│   └── custom/
├── /plugins
│   ├── sample_plugin.py
│   └── README.md
├── /assets
│   ├── nebula-logo.png
│   ├── background.jpg
│   └── gui_icons/
├── /workspace
│   └── (user files, saved projects)
├── /docs
│   ├── onboard.md
│   ├── skills.md
│   ├── architecture.md
│   ├── faq.md
│   ├── dev_guidelines.md
│   └── changelog.md
├── /tests
│   ├── test_ai_hub.py
│   ├── test_copilot_agent.py
│   ├── test_bugfinder_agent.py
│   ├── test_plugin_system.py
│   └── (expand for all future modules)
