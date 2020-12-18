"""Horizontal layout example."""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout # Lines up widgets horizontally (layout manager)
from PyQt5.QtWidgets import QPushButton # Provides a command button (widget)
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv) # Initializer
window = QWidget() # Executable widget
window.setWindowTitle("QHBoxLayout") # sets window title
layout = QHBoxLayout() # Executable layout manager
layout.addWidget(QPushButton("Left")) # adds a widget to the manager that is a button titled 'Left'
layout.addWidget(QPushButton("Center")) # adds a widget to the manager that is a button titled 'Center'
layout.addWidget(QPushButton("Right")) # adds a widget to the manager that is a button titled 'Right'
window.setLayout(layout) # sets the layout made above
window.show() # allows it to show
sys.exit(app.exec_()) # Executes the event loop until the window is closed
