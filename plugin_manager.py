import os
import importlib.util

class PluginManager:
    def __init__(self, plugin_dir='plugins'):
        self.plugin_dir = os.path.abspath(plugin_dir)
        self.plugins = []
        self.load_plugins()

    def load_plugins(self):
        self.plugins.clear()
        for fname in os.listdir(self.plugin_dir):
            if fname.endswith('.py') and not fname.startswith('_'):
                name = fname[:-3]
                path = os.path.join(self.plugin_dir, fname)
                spec = importlib.util.spec_from_file_location(name, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                self.plugins.append(mod)

    def list_plugins(self):
        return [mod.__name__ for mod in self.plugins]