"""Dialog-Style application."""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog # Dialog class
from PyQt5.QtWidgets import QDialogButtonBox #Submit buttons?
from PyQt5.QtWidgets import QFormLayout # Form layout manager
from PyQt5.QtWidgets import QLineEdit # Widgets for forms
from PyQt5.QtWidgets import QVBoxLayout # Vertical layout manager


class Dialog(QDialog): # Line 12 creates a full class Dialog for the GUI, which inherits from QDialog.
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("QDialog")
        dlgLayout = QVBoxLayout() # Sets up a vertical layout for the application  # Line 19 assigns a QVBoxLayout object to dlgLaout.
        formLayout = QFormLayout() # sets up a form layout to take in the information # Line 20 assigns a QVFormLayout object to formLayout.
        formLayout.addRow("Name:", QLineEdit()) # Line 21 to 24 add widgets to formLayout.
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        dlgLayout.addLayout(formLayout) # This adds the form layout to the vertical layout # Line 25 uses dlgLayout to arrange all the widgets on the form.
        btns = QDialogButtonBox() # setups up dialog buttons # Line 26 provides a convenient object to place the dialog buttons.
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) # 2 buttons = cancel and ok # Lines 27 and 28 add two standard buttons: Ok and Cancel.
        dlgLayout.addWidget(btns) # adds the buttons to the vertical layout
        self.setLayout(dlgLayout) # sets layout of self


if __name__ == "__main__": # Lines 32 to 36 wrap the boilerplate code in an if __name__ == '__main__': idiom. This is considered a best practice for Pythonistas.
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
