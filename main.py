# Import statements:
import sys  # why sys library? it helps to execute the main GUI window
from PyQt5.uic import loadUi # Why loadUI? used to load the .ui files to the main execution flow
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLineEdit
from validate_email import validate_email

# PyQt5 -> framework for creating GUI. QDialog, QApplication, etc are just classes of the PyQt5 library

# End of import statements


# Variables:
global loginpage_details
loginpage_details = {'admin': 'admin@password'}
global register_page_email
global register_page_password


# variable not really used, just experimenting

# Class declaration for all pages:
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("loginRegisterPage.ui",self) # loads the .ui file
        self.setWindowTitle("GrowPal")
        self.login_button.clicked.connect(self.gotologin_page) # on button click, executes the function gotologin_page()
        self.register_button.clicked.connect(self.gotoregister_page) # on button click, executes the function gotoregister_page()

    def gotologin_page(self):
        widget.setCurrentIndex(1) # Index manipulation to change the stacked screens
    def gotoregister_page(self):
        widget.setCurrentIndex(2) # Same Index manipulation stuff

class login_page(QMainWindow):
    def __init__(self):
        super(login_page,self).__init__() 
        loadUi("loginPage.ui",self) # loads the .ui file
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushbutton_login.clicked.connect(self.login_button_pressed) # button thing. directs to login_button_pressed()
        self.password_view.clicked.connect(self.pass_view_clicked)

    def pass_view_clicked(self):
        if self.password_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def back_button_pressed(self):
        widget.setCurrentIndex(0)
    def login_button_pressed(self):
        if self.lineEdit_email.text() == "" or self.lineEdit_password.text() == "": # checks if there are any empty fields
            print("empty")
        else:
            if self.lineEdit_email.text() in loginpage_details.keys():      # checking if username is in the dictionary. the .keys() function returns all the key values
                if self.lineEdit_password.text() == loginpage_details[self.lineEdit_email.text()]:     # checking if the password matches the username
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
                error_dialog.showMessage('Please create an account')                   # if username is not in the dictionary
                self.lineEdit_email.setText("")
                self.lineEdit_password.setText("")
                widget.setCurrentIndex(2)

class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerPage.ui", self) # loads the .ui file
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushbutton_register.clicked.connect(self.register_button_pressed) # button thing again
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

    def back_button_pressed(self):
        widget.setCurrentIndex(0)    
    def register_button_pressed(self):

        if self.lineEdit_username.text() == "" or self.lineEdit_email.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")   # checks for empty fields

        elif len(self.lineEdit_phnumber.text()) != 10:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Phone Number')
            error_dialog.showMessage('Please enter a valid phone number')
            self.lineEdit_phnumber.setText("")

        elif self.lineEdit_password.text() == self.lineEdit_repeatpassword.text(): # checking if both the password and confirm password fields match
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
                self.lineEdit_password.setText("")
                self.lineEdit_repeatpassword.setText("")

        elif self.lineEdit_password.text() != self.lineEdit_repeatpassword.text(): # if those two fields do not match, display an error box
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Password') # Window title for the error box
            error_dialog.showMessage('Your passwords do not match. Try again.') # message in the error box
            self.lineEdit_password.setText("")
            self.lineEdit_repeatpassword.setText("")

class buy_page(QMainWindow):
    def __init__(self) -> None:
        super(buy_page, self).__init__()
        loadUi("buy_page.ui", self) # loads the .ui file
        self.pushButton_logout.clicked.connect(self.logout)
    def logout(self):
        widget.setCurrentIndex(0)

# End of class declaration


# Indexing for stacked widget:
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() # stacked widget


main_window = MainWindow() # setting the classes as a variable for QStacked widget
loginpage = login_page() # same thing as above
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


# Exit - terminates the application when the x button is clicked

try:
    sys.exit(app.exec_())

except:
    print("Exiting")


