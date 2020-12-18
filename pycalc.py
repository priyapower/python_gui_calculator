# MVC
    # Model - coming soon
    # Controller - is class PyCalcCtrl
        # main is like a runner/index file
    # View - is class PyCalcUi

#!/usr/bin/env python3
# Above is a 'shebang line' => which defines where the interpreter is located
"""PyCalc is a simple calculator built using Python3 and PyQt5."""
import sys

from functools import partial # import this in to connect signals with methods that need to take an extra argument

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication # import the required modules and classes from PyQt5.QtWidgets
from PyQt5.QtWidgets import QMainWindow # import the required modules and classes from PyQt5.QtWidgets
from PyQt5.QtWidgets import QWidget # import the required modules and classes from PyQt5.QtWidgets
from PyQt5.QtCore import Qt # Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.
from PyQt5.QtWidgets import QGridLayout # Imports grid layout manager
from PyQt5.QtWidgets import QLineEdit # Imports text edit widgets
from PyQt5.QtWidgets import QPushButton # Import button widgets
from PyQt5.QtWidgets import QVBoxLayout # Imports vertical layout manager

__version__ = '0.1' # Is this versioning the calculator?
__author__ = 'Leodanis Pozo Ramos'  # Who is the author here? - He is one of the authors at RealPython

# ******************************VIEW******************************

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow): # creates the GUI with the class PyCalcUi. Note that this class inherits from QMainWindow
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyCalc') # sets the window’s title to PyCalc
        self.setFixedSize(235, 235) # uses .setFixedSize() to give the window a fixed size # This ensures that the user won’t be able to resize the window
        # Sets the general layout
        self.generalLayout = QVBoxLayout()
        # Set the central widget # The widget will expand to take up all the space in the window by default
        self._centralWidget = QWidget(self) # creates a QWidget object to play the role of a central widget. Remember that since your GUI class inherits from QMainWindow, you need a central widget. This object will be the parent for the rest of the GUI component.
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay() # These buttons don't work without defining the behavior (see def on ln 38)
        self._createButtons() # These buttons don't work without defining the behavior first (see def on ln 49)

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit() # create the display widget
        # Set some display's properties
        self.display.setFixedHeight(35) # The display has a fixed height of 35 pixels
        self.display.setAlignment(Qt.AlignRight) # The display shows the text as left-aligned
        self.display.setReadOnly(True) # The display is set to read-only to avoid direct editing
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display) # adds the display to the calculator’s general layout

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {} # First create an empty dictionary || datatype:dictionary - think hash from Ruby
        buttonsLayout = QGridLayout() # Use a grid layout for the buttons section
        # Button text | position on the QGridLayout
        # BELOW: Take the empty dictionary and update to hold each button's text and position (KEY = What is displayed; VALUE = Coordinates for position)
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText) # We are inside the loop here - creates the buttons and adds them to the layout
            self.buttons[btnText].setFixedSize(40, 40) # Sets every button to fixed size 40x40
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    # BUT WHAT IF YOU WANT TO UPDATE THE DICTIONARY? I MEAN - DO WE REALLY HAVE TO SET STATIC INFORMATION FOR THE BUTTONS?
        # .setDisplayText() to set and update the display’s text
        # .displayText() to get the current display’s text
        # .clearDisplay() to clear the display’s text

    def setDisplayText(self, text): # uses .setText() to set and update the display’s text, and .setFocus() to set the cursor’s focus on the display
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self): # is a getter method that returns the display’s current text. When the user clicks on the equals sign (=), the program will use the return value of .displayText() as the math expression to be evaluated
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self): # sets the display’s text to an empty string ('') so the user can introduce a new math expression
        """Clear the display."""
        self.setDisplayText('')


# BUT WHAT IF WE NEED A CONTROLLER CLASS
    # What does the controller class need to do:
        # Access the GUI’s public interface
        # Handle the creation of math expressions
        # Connect button clicked signals with the appropriate slots

# ******************************CONTROLLER******************************

# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc Controller class."""
    def __init__(self, view, model): # This is also passing the view (PyCalcUi class from ln22), but I'm unsure how? (From the tutorial: The first thing you do is give PyCalcCtrl an instance of the view PyCalcUi. You’ll use this instance to gain full access to the view’s public interface). OHHHH! When we got down to updating `main` below, I found where 'view' connects 'PyCalcUi'
        # initializing 'model' will now connect the GUI and the model (plus more work below) (we will also probably update 'main' to help this class understand what 'model' is assigned)
        """Controller initializer."""
        self._evaluate = model # sets up a self call to _evaluate to call from the model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self): # takes the display’s content, evaluate it as a math expression, and finally show the result in the display
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp): # This is going to handle the math expression
        """Build expression."""
        if self._view.displayText() == ERROR_MSG: # check if an error has occured
            self._view.clearDisplay() # If it is, clear the display
        expression = self._view.displayText() + sub_exp # also updates the calculator’s display in response to user input
        self._view.setDisplayText(expression)

    def _connectSignals(self): # connect the printable buttons with ._buildExpression() # allows your users to create math expressions by clicking on the calculator’s buttons
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))  # connect the clear button (C) to ._view.clearDisplay(). This method will clear up the text on the display.
        self._view.buttons['='].clicked.connect(self._calculateResult) # This enables the equals button
        self._view.display.returnPressed.connect(self._calculateResult) # If a user hits enter, the calculator can also process the expression (same as equals?)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

# HOWEVER - For this new controller class to work, you need to update main():

# ******************************MODEL******************************

# BUT WHAT ABOUT THE MATH? It currently doesn't do anything on 'equal'
    # So we hit the Model! It holds the data/business/math logic of an application
    # This is where the methods live to evaluate the operators used by the user
    # This is also where error handling (of the math) would occur

ERROR_MSG = 'ERROR' # sets a global variable/constraint to print string 'ERROR' # Should happen when a user introduces an invalid math expression

# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    # Thinking for the future:
        # The try...except block does NOT catch any specific exception, which is not a best practice in Python.
        # The function is based on the use of eval(), which can lead to some serious security issues. The general advice is to only use eval() on trusted input.
    try:
        result = str(eval(expression, {}, {})) # use eval() to evaluate a string as an expression
    except Exception: # If not successful
        result = ERROR_MSG # save the global variable ERROR_MSG to the result

    return result # Return the result # Automatically hits this if the 'try' is successful

# UH OH! Why doesn't the calculator work when I've added the model?
    # Well - we haven't actually finished the logic in the controller

# ******************************MAIN/RUNNER/INDEX******************************

# Client code
def main(): # defines your calculator’s main function, which is considered a best practice # This function will be the entry point to the application
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv) # creates a QApplication object pycalc
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show() # shows the GUI with view.show()
    # Create instances of the model and the controller
    model = evaluateExpression # assigns a block variable model, 
    PyCalcCtrl(view=view, model=model) # This is what tells the controller's initialize method that the 'view' comes from the PyCalcUi (the view variable that is set a few lines above)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_()) # runs the application’s event loop with pycalc.exec_()

if __name__ == '__main__':
    main()
