# Architecture

## Core Modules

- `main.py`: Application entry point
- `nebula/app.py`: Main application launcher
- `nebula/ai_hub.py`: Dynamic AI agent loader/manager
- `nebula/plugin_manager.py`: Plugin discovery and loading
- `nebula/ui/main_window.py`: Primary app UI
- `nebula/ui/agent_marketplace.py`: AI skill marketplace panel
- `nebula/ui/onboarding.py`: Onboarding wizard UI
- `nebula/ui/panels.py`: Additional UI panel components

## Directories

- `ai_agents/`: AI skill/agent files with `respond(prompt)` functions
- `plugins/`: App and UI plugin modules
- `models/`: Local LLM weights (Ollama, GPT4All, etc.)
- `docs/`: Documentation files