from PyQt5 import QtWidgets
from nebula.ui.main_window import MainWindow

def launch():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())