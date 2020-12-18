"""Simple Hello World example with PyQt5.""" # understanding the triple quotes (https://www.geeksforgeeks.org/triple-quotes-in-python/)

# Handles the exit status of the application
import sys #The sys module provides information about constants, functions and methods of the Python interpreter. (https://www.python-course.eu/sys_module.php).

# Step 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication # manages the GUI applications control flow and main settings. Contains the main event loop (where all events from the window system and other sources are processed and dispatched)
from PyQt5.QtWidgets import QLabel # Used for displaying text or an image. No user interaction functionality is provided.
from PyQt5.QtWidgets import QWidget # The base class of ass user interface object. It can receive mouse, keyboard, or other events from the window system & paint a represenation of itself on the screen

# Step 2: Create an instance of QApplication
app = QApplication(sys.argv) #Deals with initialization and gives you access to command line arguments
        # sys.argv contains the list of command-line arguments passed into a Python script. If your application is not going to accept command line arguments, then you can use an empty list instead of sys.argv. That is, you can do something like app = QApplication([]).

# Step 3. Create an instance of your application's GUI (we are using QWidget)
window = QWidget() # set a global? variable 'window' to an executable version of QWidget
window.setWindowTitle('PyQt5 App') # sets the title bar (https://doc.qt.io/qt-5/qwidget.html#top-level-and-child-widgets)
window.setGeometry(100, 100, 280, 80) # sets the geometry of the widget, relative to its parent and excluding the window frame (https://docs.huihoo.com/qt/3.3/qwidget.html#setGeometry)
        # define the size of the window and where to place it
        # .setGeometry(x, y, w, h)
        # x and y coordinates which define where the window is placed
        # w and h determine the actual width and height of the window
window.move(60, 15) # Sets the position of the widget within its parent widget (https://docs.huihoo.com/qt/3.3/qwidget.html#move)
        # .move(x, y)
        # Defines placement in the window
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window) # sets a variable that executes QLabel and makes a header on the parent window
helloMsg.move(60, 15) # Set the position of helloMsg

# NOTES
    # To avoid memory leaks, you should always make sure that any QWidget object has a parent, with the sole exception of top-level windows.
    # parent-child: A widget that doesn’t have a parent is a main window or a top-level window; A widget that has a parent (which is always another widget) is contained (or shown) within its parent.

# Step 4. Show your application's GUI
window.show() # Adds a new event to the application's event queue; shows the widget and all its children
        # if size or position has changed, this ensures move and resize has opens before it is shown

# Step 5. Run your application's event loop (or main loop)
sys.exit(app.exec_()) # The exec() call starts the event-loop and will block until the application quits. If an exit code has been set, exec() will return it after the event-loop terminates. It is good practice to pass on this exit code to sys.exit() - but it is not strictly necessary. Without the explicit call to sys.exit(), the script will automatically exit with a code of 0 after the last line of code has been executed. A non-zero exit code is usually used to inform the calling process that an error occurred.
