from PyQt6 import QtCore, QtGui, QtWidgets
from admin import Ui_AdminLoginWindow  # Import từ file admin.py
from member2 import Ui_MainWindow as MemberWindow  # Import từ file member.py
from member_management import Ui_MainWindow as ManagerWindow  # Import từ file member_management.py
from register import Ui_MainWindow as RegisterWindow  # Import từ file register.py

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 400, 80))  # Điều chỉnh kích thước và vị trí của label
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)  # Giảm kích thước font chữ
        font.setBold(True)  # Đặt chữ in đậm
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Căn giữa nội dung của label
        self.label.setObjectName("label")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 160, 700, 260))  # Điều chỉnh kích thước và vị trí của groupBox
        self.groupBox.setObjectName("groupBox")
        
        # Thiết lập CSS để bo góc và đổ màu cho các nút
        button_style = """
            QPushButton {
                background-color: #4CAF50;  /* Màu nền */
                color: white;  /* Màu chữ */
                border-radius: 7px;  /* Bo góc */
                padding: 15px 25px;  /* Khoảng cách nội dung */
            }
            
            QPushButton:hover {
                background-color: #45a049;  /* Màu nền khi di chuột */
            }
        """
        
        self.login_admin = QtWidgets.QPushButton(self.groupBox)
        self.login_admin.setGeometry(QtCore.QRect(420, 30, 180, 60))  # Điều chỉnh kích thước và vị trí của nút login_admin
        self.login_admin.setObjectName("login_admin")
        self.login_admin.setStyleSheet(button_style)
        
        self.login_member = QtWidgets.QPushButton(self.groupBox)
        self.login_member.setGeometry(QtCore.QRect(50, 30, 180, 60))  # Điều chỉnh kích thước và vị trí của nút login_member
        self.login_member.setObjectName("login_member")
        self.login_member.setStyleSheet(button_style)
        
        self.register_member = QtWidgets.QPushButton(self.groupBox)
        self.register_member.setGeometry(QtCore.QRect(50, 110, 180, 60))  # Điều chỉnh kích thước và vị trí của nút register_member
        self.register_member.setObjectName("register_member")
        self.register_member.setStyleSheet(button_style)
        
        self.manage_member = QtWidgets.QPushButton(self.groupBox)
        self.manage_member.setGeometry(QtCore.QRect(420, 110, 180, 60))  # Điều chỉnh kích thước và vị trí của nút manage_member
        self.manage_member.setObjectName("manage_member")
        self.manage_member.setStyleSheet(button_style)
        
        self.logout = QtWidgets.QPushButton(self.groupBox)
        self.logout.setGeometry(QtCore.QRect(50, 180, 180, 50))  # Điều chỉnh kích thước và vị trí của nút logout
        self.logout.setObjectName("logout")
        self.logout.setStyleSheet(button_style)
        
        mainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Main Menu"))
        self.label.setText(_translate("mainWindow", "Welcome to the System"))
        self.login_admin.setText(_translate("mainWindow", "Login as Admin"))
        self.login_member.setText(_translate("mainWindow", "Login as Member"))
        self.register_member.setText(_translate("mainWindow", "Register a New Member"))
        self.manage_member.setText(_translate("mainWindow", "Manager Members"))
        self.logout.setText(_translate("mainWindow", "Logout"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.login_admin.clicked.connect(self.open_admin_login)
        self.ui.login_member.clicked.connect(self.open_member_login)
        self.ui.register_member.clicked.connect(self.open_register_member)
        self.ui.manage_member.clicked.connect(self.open_manager_member)
        self.ui.logout.clicked.connect(self.logout)

    def open_admin_login(self):
        self.admin_window = QtWidgets.QMainWindow()
        self.admin_ui = Ui_AdminLoginWindow()
        self.admin_ui.setupUi(self.admin_window)
        self.admin_window.show()

    def open_member_login(self):
        self.member_window = QtWidgets.QMainWindow()
        self.member_ui = MemberWindow()
        self.member_ui.setupUi(self.member_window)
        self.member_window.show()

    def open_manager_member(self):
        self.manager_window = QtWidgets.QMainWindow()
        self.manager_ui = ManagerWindow()
        self.manager_ui.setupUi(self.manager_window)
        self.manager_window.show()

    def open_register_member(self):
        self.register_window = QtWidgets.QMainWindow()
        self.register_ui = RegisterWindow()
        self.register_ui.setupUi(self.register_window)
        self.register_window.show()

    def logout(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
