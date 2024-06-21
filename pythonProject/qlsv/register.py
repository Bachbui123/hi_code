from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(200, 100, 400, 400))
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 50, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;
                border-radius: 10px;
                padding: 5px;
                background-color: #ffffff;
            }
        """)
        
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 81, 20))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;
                border-radius: 10px;
                padding: 5px;
                background-color: #ffffff;
            }
        """)
        
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 91, 20))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 150, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;
                border-radius: 10px;
                padding: 5px;
                background-color: #ffffff;
            }
        """)
        
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 101, 41))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.register_member)
        self.MainWindow = MainWindow  # Store reference to the main window

    def register_member(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        
        if not username or not password or not confirm_password:
            QtWidgets.QMessageBox.warning(None, "Input Error", "All fields are required")
            return
        
        if password != confirm_password:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Passwords do not match")
            return
        
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='user_database',
                user='root',  # replace with your MySQL username
                password='Bach2003@'  # replace with your MySQL password
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Registration Successful")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            
            # Close the registration window and open the login window
            self.MainWindow.close()
            self.open_login_window()
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def open_login_window(self):
        from member2 import Ui_MainWindow as LoginWindow
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = LoginWindow()
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register"))
        self.groupBox.setTitle(_translate("MainWindow", "Register Member"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Confirm Password"))
        self.pushButton.setText(_translate("MainWindow", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
