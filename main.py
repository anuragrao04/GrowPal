import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("loginRegisterPage.ui",self)
        self.login_button.clicked.connect(self.gotologin_page)
        self.register_button.clicked.connect(self.gotoregister_page)

    def gotologin_page(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoregister_page(self):
        widget.setCurrentIndex(widget.currentIndex() + 2)

        




class login_page(QMainWindow):
    def __init__(self):
        super(login_page,self).__init__()
        loadUi("loginPage.ui",self)
        

class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerPage.ui", self)


#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(800)
widget.setFixedHeight(600)
main_window = MainWindow()
loginpage = login_page()
registerpage = register_page()
widget.addWidget(main_window)
widget.addWidget(loginpage)
widget.addWidget(registerpage)
widget.show()




try:
    sys.exit(app.exec_())

except:
    print("Exiting")
