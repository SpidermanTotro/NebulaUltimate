import importlib.util
import os

class AIHub:
    def __init__(self, agent_dir='ai_agents'):
        self.agents = {}
        self.agent_dir = os.path.abspath(agent_dir)
        self.discover_agents()

    def discover_agents(self):
        self.agents.clear()
        for fname in os.listdir(self.agent_dir):
            if fname.endswith('.py') and not fname.startswith('_'):
                agent_name = fname[:-3]
                path = os.path.join(self.agent_dir, fname)
                spec = importlib.util.spec_from_file_location(agent_name, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, 'respond'):
                    self.agents[agent_name] = mod

    def ask(self, agent, prompt):
        if agent in self.agents:
            return self.agents[agent].respond(prompt)
        return f"Agent '{agent}' not available."

    def list_agents(self):
        return list(self.agents.keys())