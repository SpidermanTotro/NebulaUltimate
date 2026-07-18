"""AI Hub module for dynamic AI agent management.

This module provides the AIHub class for discovering, loading,
and interacting with AI agent plugins.
"""

import os

from nebula.dynamic_loader import load_python_module


class AIHub:
    """Dynamic AI agent loader and manager.

    Discovers and loads AI agent modules from a specified directory,
    allowing interaction with various AI skills.

    Attributes:
        agents (dict): Dictionary mapping agent names to their modules.
        agent_dir (str): Absolute path to the agents directory.
    """

    def __init__(self, agent_dir='ai_agents'):
        """Initialize the AIHub with a directory of agents.

        Args:
            agent_dir (str): Path to the directory containing agent modules.
        """
        self.agents = {}
        self.load_errors = {}
        self.agent_dir = os.path.abspath(agent_dir)
        self.discover_agents()

    def discover_agents(self):
        """Discover and load all agent modules from the agents directory.

        Scans the agent directory for Python files with a 'respond' function
        and loads them as available agents.
        """
        self.agents.clear()
        self.load_errors.clear()
        if not os.path.isdir(self.agent_dir):
            return
        for fname in sorted(os.listdir(self.agent_dir)):
            if fname.endswith('.py') and not fname.startswith('_'):
                agent_name = fname[:-3]
                path = os.path.join(self.agent_dir, fname)
                try:
                    mod = load_python_module(agent_name, path)
                except Exception as exc:  # pylint: disable=broad-exception-caught
                    self.load_errors[agent_name] = f"{type(exc).__name__}: {exc}"
                    continue
                if hasattr(mod, 'respond'):
                    self.agents[agent_name] = mod

    def ask(self, agent, prompt):
        """Ask an agent to respond to a prompt.

        Args:
            agent (str): Name of the agent to query.
            prompt (str): The prompt or question to send to the agent.

        Returns:
            str: The agent's response, or an error message if unavailable.
        """
        if agent in self.agents:
            return self.agents[agent].respond(prompt)
        return f"Agent '{agent}' not available."

    def list_agents(self):
        """List all available agent names.

        Returns:
            list: List of agent name strings.
        """
        return list(self.agents.keys())

    def list_load_errors(self):
        """Return a copy of agent import errors keyed by agent name."""
        return dict(self.load_errors)
