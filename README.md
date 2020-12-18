# GUI Calculator with Python

This calculator creation is a demonstration of implementing an MVC (Model-View-Controller) pattern using [Python3](https://www.python.org) while also using [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/introduction.html) - a set of python bindings that gives us access to GUI code (bridging from C++ to Python).

The calculator can apply basic math operations such as addition, subtraction, multiplication, and division as well as nested operations using parentheses.

## Requirements
- Python3 >= 3.6
- Pip3
- PyQt5 library
  - One way to install:
  ```console
  $ sudo pip3 install pyqt5
  ```
  - Using a virtual environment (the difference between loading it on your entire system vs just your project space)
  ```console
  $ python3 -m venv pycalc
  $ source pycalc/bin/activate
  $ pip install pyqt5
  ```
- To check installation, run testing below

## Running and Using the Calculator
- Execute
  ```console
  $ python3 pycalc.py
  ```
- A calculator application should open
- Enter any valid math expressions using your mouse and click `=` ** OR ** enter math expressions with your keyboard and press `Enter`/`Return`

## License

PyCalc is released under the [MIT License](https://opensource.org/licenses/MIT).
