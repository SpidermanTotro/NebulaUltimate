"""Tests for local agent and plugin discovery boundaries."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from nebula.ai_hub import AIHub
from nebula.plugin_manager import PluginManager


class AIHubTests(unittest.TestCase):
    """Verify that one invalid local agent cannot break discovery."""

    def test_missing_directory_is_empty(self):
        """A missing optional agent directory should produce an empty hub."""
        with TemporaryDirectory() as temp_dir:
            hub = AIHub(str(Path(temp_dir) / "missing"))

        self.assertEqual(hub.list_agents(), [])
        self.assertEqual(hub.list_load_errors(), {})

    def test_discovers_agents_deterministically_and_isolates_failures(self):
        """Valid agents load in name order while broken files are reported."""
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "zeta.py").write_text(
                "def respond(prompt):\n    return f'zeta:{prompt}'\n",
                encoding="utf-8",
            )
            (root / "alpha.py").write_text(
                "def respond(prompt):\n    return f'alpha:{prompt}'\n",
                encoding="utf-8",
            )
            (root / "helper.py").write_text("VALUE = 1\n", encoding="utf-8")
            (root / "broken.py").write_text("def nope(:\n", encoding="utf-8")
            (root / "_private.py").write_text(
                "def respond(prompt):\n    return prompt\n",
                encoding="utf-8",
            )

            hub = AIHub(temp_dir)

        self.assertEqual(hub.list_agents(), ["alpha", "zeta"])
        self.assertEqual(hub.ask("alpha", "hello"), "alpha:hello")
        self.assertEqual(hub.ask("missing", "hello"), "Agent 'missing' not available.")
        self.assertIn("SyntaxError", hub.list_load_errors()["broken"])


class PluginManagerTests(unittest.TestCase):
    """Verify deterministic plugin discovery and failure isolation."""

    def test_loads_valid_plugins_and_reports_invalid_plugins(self):
        """One failed plugin import must not prevent valid plugins loading."""
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "second.py").write_text("VALUE = 2\n", encoding="utf-8")
            (root / "first.py").write_text("VALUE = 1\n", encoding="utf-8")
            (root / "broken.py").write_text("raise RuntimeError('broken')\n", encoding="utf-8")
            (root / "_private.py").write_text("VALUE = 0\n", encoding="utf-8")

            manager = PluginManager(temp_dir)

        self.assertEqual(manager.list_plugins(), ["first", "second"])
        self.assertEqual(manager.plugins[0].VALUE, 1)
        self.assertIn("RuntimeError: broken", manager.list_load_errors()["broken"])


if __name__ == "__main__":
    unittest.main()
