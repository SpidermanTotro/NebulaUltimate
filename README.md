# Nebula Ultimate

**Free, Offline, Open and Infinitely Expandable Development Platform**

## Overview

Nebula Ultimate is an offline AI-powered development platform with support for
various AI agents/skills that can be dynamically loaded and used.

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Run local LLM server (e.g., Ollama with codellama)
3. Launch the application: `python main.py`

## AI Skills

Add skills by dropping `.py` files with a `respond(prompt)` function in the `/ai_agents` folder.
They appear automatically on next launch.

## Project Structure

See [architecture.md](architecture.md) for details on project structure.

## Documentation

- [Onboarding Guide](onboard.md)
- [FAQ](faq.md)
- [Developer Guidelines](dev_guidelines.md)
- [Skills Reference](skills.md)
- [Changelog](changelog.md)

## Historical material

The [legacy installation page](docs/archive/legacy-install-page.html) from the earlier malformed-name repository is preserved for reference. Its download links and feature claims are historical and are not verified instructions for the current project.
