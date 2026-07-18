"""Plugin Manager module for Nebula Ultimate.

This module provides the PluginManager class for discovering and loading
plugin modules from a specified directory.
"""

import os

from nebula.dynamic_loader import load_python_module


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
        self.load_errors = {}
        self.load_plugins()

    def load_plugins(self):
        """Load all plugin modules from the plugins directory.

        Scans the plugin directory for Python files and loads them
        as available plugins.
        """
        self.plugins.clear()
        self.load_errors.clear()
        if not os.path.isdir(self.plugin_dir):
            return
        for fname in sorted(os.listdir(self.plugin_dir)):
            if fname.endswith('.py') and not fname.startswith('_'):
                name = fname[:-3]
                path = os.path.join(self.plugin_dir, fname)
                try:
                    mod = load_python_module(name, path)
                except Exception as exc:  # pylint: disable=broad-exception-caught
                    self.load_errors[name] = f"{type(exc).__name__}: {exc}"
                    continue
                self.plugins.append(mod)

    def list_plugins(self):
        """List all loaded plugin names.

        Returns:
            list: List of plugin module name strings.
        """
        return [mod.__name__ for mod in self.plugins]

    def list_load_errors(self):
        """Return a copy of plugin import errors keyed by plugin name."""
        return dict(self.load_errors)
