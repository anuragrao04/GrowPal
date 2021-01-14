from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(100, 100, 960, 540)
win.setWindowTitle("GrowPal")
win.show()
sys.exit(app.exec_())


