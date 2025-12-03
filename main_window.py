from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QMenuBar
from nebula.ai_hub import AIHub

class MainWindow(QMainWindow):
    def __init__(self):
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
            action.triggered.connect(lambda checked, agent=agent: self.ask_ai(agent))
            ai_menu.addAction(action)
        self.setMenuBar(self.menu)

    def ask_ai(self, agent):
        prompt, ok = self._get_user_text("Ask Copilot", f"Prompt for {agent}:")
        if ok and prompt:
            result = self.ai_hub.ask(agent, prompt)
            self.text.append(f"🧑‍💻 [{agent}]\n{result}\n")

    def _get_user_text(self, title, desc):
        from PyQt5.QtWidgets import QInputDialog
        text, ok = QInputDialog.getText(self, title, desc)
        return text, ok