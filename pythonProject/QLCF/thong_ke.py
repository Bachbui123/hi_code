from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(240, 120, 441, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 91, 31))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 120, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 260, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(644, 422, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 320, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 50, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 50, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to their respective functions
        self.pushButton.clicked.connect(self.show_7_days_data)
        self.pushButton_2.clicked.connect(self.show_1_day_data)
        self.pushButton_3.clicked.connect(self.show_30_days_data)
        self.pushButton_5.clicked.connect(self.show_total_data)
        self.pushButton_6.clicked.connect(self.filter_data)
        self.pushButton_4.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "7 Ngày"))
        self.pushButton_2.setText(_translate("MainWindow", "1 Ngày"))
        self.pushButton_3.setText(_translate("MainWindow", "30 Ngày"))
        self.pushButton_4.setText(_translate("MainWindow", "Thoát"))
        self.pushButton_5.setText(_translate("MainWindow", "Tổng"))
        self.pushButton_6.setText(_translate("MainWindow", "Lọc"))

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='quanli_quan_game',
                user='root',
                password='Bach2003@'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print("Error while connecting to MySQL", e)
            return None

    def show_1_day_data(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM thong_ke_ngan_sach WHERE ngay = (SELECT MIN(ngay) FROM thong_ke_ngan_sach WHERE ngay = CURDATE()) ORDER BY id ASC")
            result = cursor.fetchall()
            self.plainTextEdit.clear()
            for row in result:
                self.plainTextEdit.appendPlainText(f"ID: {row[0]}, Ngày: {row[1]}, Tiền thuê máy: {row[2]}, Đồ ăn: {row[3]}, Nước uống: {row[4]}, Dịch vụ khác: {row[5]}")
            cursor.close()
            connection.close()

    def show_7_days_data(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM thong_ke_ngan_sach WHERE ngay >= (SELECT MIN(ngay) FROM thong_ke_ngan_sach WHERE ngay >= CURDATE() - INTERVAL 7 DAY) ORDER BY id ASC")
            result = cursor.fetchall()
            self.plainTextEdit.clear()
            for row in result:
                self.plainTextEdit.appendPlainText(f"ID: {row[0]}, Ngày: {row[1]}, Tiền thuê máy: {row[2]}, Đồ ăn: {row[3]}, Nước uống: {row[4]}, Dịch vụ khác: {row[5]}")
            cursor.close()
            connection.close()

    def show_30_days_data(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM thong_ke_ngan_sach WHERE ngay >= (SELECT MIN(ngay) FROM thong_ke_ngan_sach WHERE ngay >= CURDATE() - INTERVAL 30 DAY) ORDER BY id ASC")
            result = cursor.fetchall()
            self.plainTextEdit.clear()
            for row in result:
                self.plainTextEdit.appendPlainText(f"ID: {row[0]}, Ngày: {row[1]}, Tiền thuê máy: {row[2]}, Đồ ăn: {row[3]}, Nước uống: {row[4]}, Dịch vụ khác: {row[5]}")
            cursor.close()
            connection.close()

    def show_total_data(self):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM thong_ke_ngan_sach ORDER BY id ASC")
            result = cursor.fetchall()
            self.plainTextEdit.clear()
            for row in result:
                self.plainTextEdit.appendPlainText(f"ID: {row[0]}, Ngày: {row[1]}, Tiền thuê máy: {row[2]}, Đồ ăn: {row[3]}, Nước uống: {row[4]}, Dịch vụ khác: {row[5]}")
            cursor.close()
            connection.close()

    def filter_data(self):
        text = self.lineEdit.text()
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM thong_ke_ngan_sach WHERE ghi_chu LIKE '%{text}%' ORDER BY id ASC"
            cursor.execute(query)
            result = cursor.fetchall()
            self.plainTextEdit.clear()
            for row in result:
                self.plainTextEdit.appendPlainText(f"ID: {row[0]}, Ngày: {row[1]}, Tiền thuê máy: {row[2]}, Đồ ăn: {row[3]}, Nước uống: {row[4]}, Dịch vụ khác: {row[5]}")
            cursor.close()
            connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
