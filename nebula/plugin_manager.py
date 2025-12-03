"""Plugin Manager module for Nebula Ultimate.

This module provides the PluginManager class for discovering and loading
plugin modules from a specified directory.
"""

import os
import importlib.util


class PluginManager:
    """Manager for loading and handling application plugins.

    Discovers and loads plugin modules from a specified directory,
    providing access to their functionality.

    Attributes:
        plugin_dir (str): Absolute path to the plugins directory.
        plugins (list): List of loaded plugin modules.
    """

    def __init__(self, plugin_dir='plugins'):
        """Initialize the PluginManager with a directory of plugins.

        Args:
            plugin_dir (str): Path to the directory containing plugin modules.
        """
        self.plugin_dir = os.path.abspath(plugin_dir)
        self.plugins = []
        self.load_plugins()

    def load_plugins(self):
        """Load all plugin modules from the plugins directory.

        Scans the plugin directory for Python files and loads them
        as available plugins.
        """
        self.plugins.clear()
        if not os.path.exists(self.plugin_dir):
            return
        for fname in os.listdir(self.plugin_dir):
            if fname.endswith('.py') and not fname.startswith('_'):
                name = fname[:-3]
                path = os.path.join(self.plugin_dir, fname)
                spec = importlib.util.spec_from_file_location(name, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                self.plugins.append(mod)

    def list_plugins(self):
        """List all loaded plugin names.

        Returns:
            list: List of plugin module name strings.
        """
        return [mod.__name__ for mod in self.plugins]
