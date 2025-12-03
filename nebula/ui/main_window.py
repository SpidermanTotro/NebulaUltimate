"""Main window module for Nebula Ultimate UI.

This module provides the MainWindow class, the primary application window
for the Nebula Ultimate development platform.
"""

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QMenuBar, QInputDialog
from nebula.ai_hub import AIHub


class MainWindow(QMainWindow):
    """Main application window for Nebula Ultimate.

    Provides the primary user interface including a text editor area
    and AI skills menu for interacting with various AI agents.

    Attributes:
        text (QTextEdit): The central text editing widget.
        ai_hub (AIHub): The AI agent hub for managing AI interactions.
        menu (QMenuBar): The application menu bar.
    """

    def __init__(self):
        """Initialize the main window with AI skills menu."""
        super().__init__()
        self.setWindowTitle("Nebula Ultimate - Offline Copilot AI Dev Platform")
        self.setGeometry(200, 200, 1000, 800)
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)
        self.ai_hub = AIHub(agent_dir='ai_agents')

        # Menubar for AI Skills
        self.menu = QMenuBar(self)
        ai_menu = self.menu.addMenu("AI Skills")
        for agent in self.ai_hub.list_agents():
            action = QAction(agent, self)
            action.triggered.connect(lambda checked, a=agent: self.ask_ai(a))
            ai_menu.addAction(action)
        self.setMenuBar(self.menu)

    def ask_ai(self, agent):
        """Prompt the user and query an AI agent.

        Args:
            agent (str): Name of the AI agent to query.
        """
        prompt, ok = self._get_user_text("Ask Copilot", f"Prompt for {agent}:")
        if ok and prompt:
            result = self.ai_hub.ask(agent, prompt)
            self.text.append(f"🧑‍💻 [{agent}]\n{result}\n")

    def _get_user_text(self, title, desc):
        """Display an input dialog to get user text.

        Args:
            title (str): Dialog window title.
            desc (str): Description/prompt for the input.

        Returns:
            tuple: (text, ok) where text is the user input and ok is boolean.
        """
        text, ok = QInputDialog.getText(self, title, desc)
        return text, ok
