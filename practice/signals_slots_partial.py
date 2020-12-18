"""Signals and slots example."""
import functools # For this code to work, you need to import functools first (the partial language)
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting(who):
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}") # Now, greeting() needs to receive an argument called who.


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals, and Slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(functools.partial(greeting, "World!")) # connect this new version of greeting() to the btn.clicked signal # If your slot function needs to receive extra arguments, then you can pass them in by using functools.partial.
# TRY CHANGING "World!" AND SEE WHAT HAPPENS!!!! => This is the "dynamic" variable declaration

layout.addWidget(btn)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
