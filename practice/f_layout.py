"""Form layout example."""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout # Imports the form layout manager class
from PyQt5.QtWidgets import QLineEdit # Widget that allows for text editable sections (aka, the form)
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QFormLayout")
layout = QFormLayout() # Executable form class
layout.addRow("Name:", QLineEdit()) # Adds labeled forms
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
