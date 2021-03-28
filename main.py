#Import statements:
import sys #why sys library? it helps to execute the main GUI window
from PyQt5.uic import loadUi #Why loadUI? used to load the .ui files to the main execution flow 
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from validate_email import validate_email

#PyQt5 -> framework for creating GUI. QDialog, QApplication, etc are just modules of the PyQt5 library

#End of import statements 


#Variables:
global dictionary_email_password
dictionary_email_password = {'admin':'admin@password'} 
global register_page_email
global register_page_password


#variable not really used, just experimenting

#Class declaration for all pages:
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("loginRegisterPage.ui",self) #loads the .ui file 
        self.login_button.clicked.connect(self.gotologin_page) #on button click, executes the function gotologin_page()
        self.register_button.clicked.connect(self.gotoregister_page) #on button click, executes the function gotoregister_page()

    def gotologin_page(self):
        widget.setCurrentIndex(1) #Index manipulation to change the stacked screens 
    def gotoregister_page(self):
        widget.setCurrentIndex(2) #Same Index manipulation stuff 





class login_page(QMainWindow):
    def __init__(self):
        super(login_page,self).__init__() 
        loadUi("loginPage.ui",self) #loads the .ui file 
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushbutton_login.clicked.connect(self.login_button_pressed) #button thing. directs to login_button_pressed() 
    def back_button_pressed(self):
        widget.setCurrentIndex(0)
    def login_button_pressed(self):
        if self.lineEdit_email.text() == "" or self.lineEdit_password.text() == "": #checks if there are any empty fields 
            print("empty")
        
        else:
            if self.lineEdit_email.text() in dictionary_email_password.keys():      #checking if username is in the dictionary. the .keys() function returns all the key values

                if self.lineEdit_password.text() == dictionary_email_password[self.lineEdit_email.text()]:     #checking if the password matches the username 
                    widget.setCurrentIndex(3)
                    

                else: 
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Password')
                    error_dialog.showMessage('Incorrect password, please try again')


                    
                     
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Account')
                error_dialog.showMessage('Please create an account')                   #if username is not in the dictionary 
                widget.setCurrentIndex(2)   
            
    
        

class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerPage.ui", self) #loads the .ui file 
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushbutton_register.clicked.connect(self.register_button_pressed) #button thing again
    def back_button_pressed(self):
        widget.setCurrentIndex(0)    
    def register_button_pressed(self): 
        if self.lineEdit_email.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")   #checks for empty fields 
        elif len(self.lineEdit_phnumber.text()) != 10:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Phone Number')
            error_dialog.showMessage('Please enter a valid phone number')



        elif self.lineEdit_password.text() == self.lineEdit_repeatpassword.text(): #checking if both the password and confirm password fields match
           
            if validate_email(self.lineEdit_email.text()):
                
                
                register_page_email = self.lineEdit_email.text()
                register_page_password = self.lineEdit_password.text()
                dictionary_email_password.update({register_page_email:register_page_password})
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Thanks!')
                error_dialog.showMessage('Thanks for creating an account with us! Please login with the same credentials')
                widget.setCurrentIndex(1)
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Email')
                error_dialog.showMessage('Please enter a valid email ID')


        elif self.lineEdit_password.text() != self.lineEdit_repeatpassword.text(): #if those two fields do not match, display an error box
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Password') #Window title for the error box
            error_dialog.showMessage('Your passwords do not match. Try again.') #message in the error box 
class buy_page(QMainWindow): 
    def __init__(self) -> None:
        super(buy_page, self).__init__()
        loadUi("buy_page.ui", self) #loads the .ui file 
        self.pushButton_logout.clicked.connect(self.logout)
    def logout(self):
        widget.setCurrentIndex(0)
#End of class declaration


#Indexing for stacked widget:
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() #stacked widget 
widget.setFixedWidth(800) #setting mainwindow size
widget.setFixedHeight(600)
main_window = MainWindow() #setting the classes as a variable for QStacked widget 
loginpage = login_page() #same thing as above
buypage = buy_page()
registerpage = register_page()
widget.addWidget(main_window) #0        #Indexing for all the stacked pages. indexes are appointed in the order they are added. 
widget.addWidget(loginpage)   #1
widget.addWidget(registerpage)#2
widget.addWidget(buypage)     #3
#End of indexing for stacked widgets 


#Execution:
widget.show()


#Exit - terminates the application when the x button is clicked 

try:
    sys.exit(app.exec_())

except:
    print("Exiting")


