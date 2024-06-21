import sys
from PyQt6 import QtWidgets, QtGui, QtCore
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 753)
        MainWindow.setStyleSheet("background-color: rgb(230, 255, 248);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 230, 641, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 497, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 178, 123);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_employee)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 497, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 172, 139);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.edit_employee)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 497, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 147, 111);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.delete_employee)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 497, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 138, 114);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(QtWidgets.QApplication.quit)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 120, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 166, 114);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.search_employee)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 120, 271, 51))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bach2003@",
            database="nv_db"
        )
        self.cursor = self.conn.cursor()
        self.load_data()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Nv"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phòng ban"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mức lương theo ngày "))
        self.pushButton.setText(_translate("MainWindow", "Thêm"))
        self.pushButton_2.setText(_translate("MainWindow", "Sửa"))
        self.pushButton_3.setText(_translate("MainWindow", "Xóa"))
        self.pushButton_4.setText(_translate("MainWindow", "Thoát"))
        self.pushButton_5.setText(_translate("MainWindow", "Tìm kiếm"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Nhập tên hoặc mã nhân viên "))
        self.label.setText(_translate("MainWindow", "Danh sách nhân viên "))

    def load_data(self):
        self.cursor.execute("SELECT * FROM NhanVien")
        rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_employee(self):
        ma_nv, ok = QtWidgets.QInputDialog.getInt(self.centralwidget, "Thêm Nhân Viên", "Mã NV:")
        if not ok:
            return
        ho_ten, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "Thêm Nhân Viên", "Họ tên:")
        if not ok:
            return
        phong_ban, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "Thêm Nhân Viên", "Phòng ban:")
        if not ok:
            return
        muc_luong_theo_ngay, ok = QtWidgets.QInputDialog.getDouble(self.centralwidget, "Thêm Nhân Viên", "Mức lương theo ngày:")
        if not ok:
            return

        self.cursor.execute("INSERT INTO NhanVien (MaNV, HoTen, PhongBan, MucLuongTheoNgay) VALUES (%s, %s, %s, %s)",
                            (ma_nv, ho_ten, phong_ban, muc_luong_theo_ngay))
        self.conn.commit()
        self.load_data()

    def edit_employee(self):
        selected = self.tableWidget.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Chọn nhân viên để sửa")
            return
        ma_nv = int(self.tableWidget.item(selected, 0).text())

        ho_ten, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "Sửa Nhân Viên", "Họ tên:", text=self.tableWidget.item(selected, 1).text())
        if not ok:
            return
        phong_ban, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "Sửa Nhân Viên", "Phòng ban:", text=self.tableWidget.item(selected, 2).text())
        if not ok:
            return
        muc_luong_theo_ngay, ok = QtWidgets.QInputDialog.getDouble(self.centralwidget, "Sửa Nhân Viên", "Mức lương theo ngày:", value=float(self.tableWidget.item(selected, 3).text()))
        if not ok:
            return

        self.cursor.execute("UPDATE NhanVien SET HoTen=%s, PhongBan=%s, MucLuongTheoNgay=%s WHERE MaNV=%s",
                            (ho_ten, phong_ban, muc_luong_theo_ngay, ma_nv))
        self.conn.commit()
        self.load_data()

    def delete_employee(self):
        selected = self.tableWidget.currentRow()
        if selected < 0:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Chọn nhân viên để xóa")
            return
        ma_nv = int(self.tableWidget.item(selected, 0).text())
        confirm = QtWidgets.QMessageBox.question(self.centralwidget, "Xác nhận xóa", "Bạn có chắc muốn xóa nhân viên này?", 
                                                  QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            self.cursor.execute("DELETE FROM NhanVien WHERE MaNV = %s", (ma_nv,))
            self.conn.commit()
            self.load_data()


    def search_employee(self):
        search_text = self.textEdit.toPlainText().strip()
        if not search_text:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Nhập tên hoặc mã nhân viên để tìm kiếm")
            return

        query = "SELECT * FROM NhanVien WHERE MaNV LIKE %s OR HoTen LIKE %s"
        self.cursor.execute(query, (f'%{search_text}%', f'%{search_text}%'))
        rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
