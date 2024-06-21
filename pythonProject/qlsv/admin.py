from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_AdminLoginWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow  # Lưu tham chiếu tới MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 130, 521, 291))
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.username = QtWidgets.QLineEdit(parent=self.groupBox)
        self.username.setGeometry(QtCore.QRect(190, 70, 191, 31))
        self.username.setObjectName("username")
        self.username.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;  /* Viền */
                border-radius: 10px;  /* Bo góc */
                padding: 5px;  /* Khoảng cách nội dung */
                background-color: #ffffff;  /* Màu nền */
            }
        """)
        
        self.login_admin = QtWidgets.QPushButton(parent=self.groupBox)
        self.login_admin.setGeometry(QtCore.QRect(170, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.login_admin.setFont(font)
        self.login_admin.setObjectName("login_admin")
        
        # Áp dụng CSS để bo góc và đổi màu cho nút login_admin
        self.login_admin.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  /* Màu nền */
                color: white;  /* Màu chữ */
                border-radius: 10px;  /* Bo góc */
                padding: 10px 20px;  /* Khoảng cách nội dung */
                border: none;  /* Bỏ viền */
            }
            
            QPushButton:hover {
                background-color: #45a049;  /* Màu nền khi di chuột */
            }
        """)

        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 81, 20))
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.password = QtWidgets.QLineEdit(parent=self.groupBox)
        self.password.setGeometry(QtCore.QRect(190, 140, 191, 31))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;  /* Viền */
                border-radius: 10px;  /* Bo góc */
                padding: 5px;  /* Khoảng cách nội dung */
                background-color: #ffffff;  /* Màu nền */
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
        
        self.login_admin.clicked.connect(self.login_as_admin)

        # Kết nối MySQL và tạo bảng admin
        self.create_admin_table()

    def create_admin_table(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Bach2003@",
                database="user_database"
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS admin (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def login_as_admin(self):
        username = self.username.text()
        password = self.password.text()

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Bach2003@",
                database="user_database"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
            result = mycursor.fetchone()
            mycursor.close()
            mydb.close()

            if result:
                QtWidgets.QMessageBox.information(None, "Success", "Đăng nhập thành công!")
                self.open_member_management()
            else:
                QtWidgets.QMessageBox.critical(None, "Failure", "Đăng nhập thất bại!")
        except mysql.connector.Error as err:
            print("Error:", err)

    def open_member_management(self):
        from member_management import Ui_MainWindow as MemberManagementWindow
        self.member_management_window = QtWidgets.QMainWindow()
        self.member_management_ui = MemberManagementWindow()
        self.member_management_ui.setupUi(self.member_management_window)
        self.MainWindow.close()
        self.member_management_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Đăng nhập quản trị viên"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.login_admin.setText(_translate("MainWindow", "Đăng nhập"))
        self.label_2.setText(_translate("MainWindow", "Password"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminLoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
