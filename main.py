# Import statements:
import sys  
#pip install PyQt5
from PyQt5.uic import loadUi 
from PyQt5 import QtWidgets
from PyQt5 import QtGui  
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLineEdit
from validate_email import validate_email
#pip install validate_email


# Variables:
global loginpage_details
loginpage_details = {'admin': 'admin@password'}
global register_page_email
global register_page_password




# Class declaration for all pages:
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("loginRegisterPage.ui",self) 
        self.setWindowTitle("GrowPal")
        self.login_button.clicked.connect(self.gotologin_page) 
        self.register_button.clicked.connect(self.gotoregister_page) 
        self.iconName = "logo.jpg"
    def gotologin_page(self):
        widget.setCurrentIndex(1) 
    def gotoregister_page(self):
        widget.setCurrentIndex(2)

class login_page(QMainWindow):
    def __init__(self):
        super(login_page,self).__init__() 
        loadUi("loginPage.ui",self) 
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushbutton_login.clicked.connect(self.login_button_pressed) 
        self.password_view.clicked.connect(self.pass_view_clicked)

    def pass_view_clicked(self):
        if self.password_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def back_button_pressed(self):
        widget.setCurrentIndex(0)


    def login_button_pressed(self):
        if self.lineEdit_email.text() == "" or self.lineEdit_password.text() == "": 
            print("empty")
        else:
            if self.lineEdit_email.text() in loginpage_details.keys():     
                if self.lineEdit_password.text() == loginpage_details[self.lineEdit_email.text()]:     
                    self.lineEdit_email.setText("")
                    self.lineEdit_password.setText("")
                    widget.setCurrentIndex(3)
                else: 
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Password')
                    error_dialog.showMessage('Incorrect password, please try again')
                    self.lineEdit_password.setText("")
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Account')
                error_dialog.showMessage('Please create an account')                  
                self.lineEdit_email.setText("")
                self.lineEdit_password.setText("")
                widget.setCurrentIndex(2)



class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerPage.ui", self) 
        self.pushButton_back.clicked.connect(self.back_button_clicked)
        self.pushbutton_register.clicked.connect(self.register_button_clicked) 
        self.sp_view.clicked.connect(self.sp_view_clicked)
        self.cp_view.clicked.connect(self.cp_view_clicked)
       
        



    def sp_view_clicked(self):
        if self.sp_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)



    def cp_view_clicked(self):
        if self.cp_view.isChecked():
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Password)


    def back_button_clicked(self):
        widget.setCurrentIndex(0)


    def register_button_clicked(self):
       

        if self.lineEdit_username.text() == "" or self.lineEdit_email.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")  

        elif len(self.lineEdit_phnumber.text()) != 10:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Phone Number')
            error_dialog.showMessage('Please enter a valid phone number')
            self.lineEdit_phnumber.setText("")

        elif self.lineEdit_password.text() == self.lineEdit_repeatpassword.text(): 
            if validate_email(self.lineEdit_email.text()):
                register_page_username = self.lineEdit_username.text()
                register_page_password = self.lineEdit_password.text()
                loginpage_details.update({register_page_username:register_page_password})
                self.lineEdit_password.setText("")
                self.lineEdit_repeatpassword.setText("")
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Thanks!')
                error_dialog.showMessage('Thanks for creating an account with us! Please login with the same credentials')
                widget.setCurrentIndex(1)
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Email')
                error_dialog.showMessage('Please enter a valid email ID')
                self.lineEdit_email.setText("")



        elif self.lineEdit_password.text() != self.lineEdit_repeatpassword.text(): 
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Password') 
            error_dialog.showMessage('Your passwords do not match. Try again.') 
            self.lineEdit_password.setText("")
            self.lineEdit_repeatpassword.setText("")

class buy_page(QMainWindow):
    def __init__(self) -> None:
        super(buy_page, self).__init__()
        loadUi("buy_page.ui", self)
        self.pushButton_logout.clicked.connect(self.logout)
    def logout(self):
        widget.setCurrentIndex(0)

# End of class declaration


# Indexing for stacked widget:
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() 


main_window = MainWindow() 
loginpage = login_page() 
buypage = buy_page()
registerpage = register_page()
# Indexing for all the stacked pages. indexes are appointed in the order they are added.
widget.addWidget(main_window) # 0
widget.addWidget(loginpage)   # 1
widget.addWidget(registerpage) # 2
widget.addWidget(buypage)     # 3
# End of indexing for stacked widgets


# Execution:
widget.show()


# Exit 

try:
    sys.exit(app.exec_())

except:
    print("Exiting")


