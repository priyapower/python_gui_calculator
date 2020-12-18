"""Main Window-Style application."""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class Window(QMainWindow): # Line 10 creates a class Window that inherits from QMainWindow.
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("QMainWindow") # Line 15 sets the window’s title.
        self.setCentralWidget(QLabel("I'm the Central Widget")) # Line 16 sets a QLabel as the central widget.
        self._createMenu() # Lines 17 to 19 call private methods in the lines that follow in order to create different GUI elements
        self._createToolBar() # Lines 17 to 19 call private methods in the lines that follow in order to create different GUI elements
        self._createStatusBar() # Lines 17 to 19 call private methods in the lines that follow in order to create different GUI elements

    def _createMenu(self): # Lines 21 to 23 create the main menu.
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction("&Exit", self.close)

    def _createToolBar(self): # Lines 25 to 28 create the toolbar.
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createStatusBar(self): # Lines 30 to 33 create the status bar.
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
