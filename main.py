# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow

class Robert(QMainWindow):
	def __init__(self):
		super(Robert, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)

    window = Robert()
    window.ui.pushButton.clicked.connect(app.quit)
    window.show()

    sys.exit(app.exec())

