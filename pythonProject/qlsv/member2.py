from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 120, 501, 331))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("""
            QGroupBox {
                background-color: #f0f0f0;  /* Màu nền */
                border: 2px solid #d3d3d3;  /* Viền */
                border-radius: 15px;  /* Bo góc */
                margin-top: 20px;  /* Khoảng cách từ trên xuống của tiêu đề */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;  /* Vị trí của tiêu đề */
                padding: 0 3px;
            }
        """)
        
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 90, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;  /* Viền */
                border-radius: 10px;  /* Bo góc */
                padding: 5px;  /* Khoảng cách nội dung */
                background-color: #ffffff;  /* Màu nền */
            }
        """)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 140, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setStyleSheet("""
            QLineEdit {
                border: 2px solid #d3d3d3;  /* Viền */
                border-radius: 10px;  /* Bo góc */
                padding: 5px;  /* Khoảng cách nội dung */
                background-color: #ffffff;  /* Màu nền */
            }
        """)
        
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Đăng nhập thành viên"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Đăng nhập"))

        # Kết nối sự kiện click của button Đăng nhập với hàm handle_login
        self.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập tên đăng nhập và mật khẩu.")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Bach2003@",
                database="user_database"
            )
            cursor = db.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            db.close()

            if result:
                QtWidgets.QMessageBox.information(None, "Thành công", "Đăng nhập thành công!")
                # Bạn có thể thêm mã để mở cửa sổ mới hoặc thực hiện các hành động khác ở đây
            else:
                QtWidgets.QMessageBox.warning(None, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.")
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Lỗi cơ sở dữ liệu", f"Lỗi xảy ra: {err}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
