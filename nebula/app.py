"""Application module for Nebula Ultimate.

This module provides the main entry point for launching the application.
"""

from PyQt5 import QtWidgets
from nebula.ui.main_window import MainWindow


def launch():
    """Launch the Nebula Ultimate application.

    Creates the Qt application instance, displays the main window,
    and starts the event loop.
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
