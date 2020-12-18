"""Vertical layout example."""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout # # Lines up widgets vertically (layout manager)
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QVBoxLayout")
layout = QVBoxLayout() # Makes an executable variable using the Vertical Layout Manager Class
layout.addWidget(QPushButton("Top")) # Top button
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Bottom"))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
