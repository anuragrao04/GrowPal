import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication



class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("loginRegisterPage.ui",self)
        self.register_button.clicked.connect(self.gotologin_page)

    def gotologin_page(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)




class login_page(QDialog):
    def __init__(self):
        super(login_page,self).__init__()
        loadUi("loginPage",self)



#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = MainWindow()
loginpage = login_page()
widget.addWidget(main_window)
widget.addWidget(loginpage)



try:
    sys.exit(app.exec_())

except:
    print("Exiting")