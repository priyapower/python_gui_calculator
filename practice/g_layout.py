"""Grid layout example."""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout # Imports the Grid Layout Manager class
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QGridLayout")
layout = QGridLayout() # Here is the grid class manager
layout.addWidget(QPushButton("Button (0, 0)"), 0, 0) # The String defines the title of the button; # The Integers define the position
layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
layout.addWidget(QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2) # The integers here represent 2 column span - but why isn't it: 2, 1, 2, 2?. when I experimented and put that in, it brought the double span button a little further down the grid (off kilter with button (2,0))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
