from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class AddEmployeeDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thêm Nhân Viên")
        self.setGeometry(300, 300, 400, 300)

        self.name_label = QtWidgets.QLabel("Họ Tên:", self)
        self.name_label.setGeometry(QtCore.QRect(30, 50, 60, 30))
        self.name_text = QtWidgets.QLineEdit(self)
        self.name_text.setGeometry(QtCore.QRect(100, 50, 200, 30))

        self.phong_ban_label = QtWidgets.QLabel("Phòng Ban:", self)
        self.phong_ban_label.setGeometry(QtCore.QRect(30, 100, 60, 30))
        self.phong_ban_text = QtWidgets.QLineEdit(self)
        self.phong_ban_text.setGeometry(QtCore.QRect(100, 100, 200, 30))

        self.luong_label = QtWidgets.QLabel("Lương:", self)
        self.luong_label.setGeometry(QtCore.QRect(30, 150, 60, 30))
        self.luong_text = QtWidgets.QLineEdit(self)
        self.luong_text.setGeometry(QtCore.QRect(100, 150, 200, 30))

        self.add_button = QtWidgets.QPushButton("Thêm", self)
        self.add_button.setGeometry(QtCore.QRect(150, 200, 100, 30))
        self.add_button.clicked.connect(self.accept)

    def get_data(self):
        return self.name_text.text(), self.phong_ban_text.text(), float(self.luong_text.text())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 210, 381, 231))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.them = QtWidgets.QPushButton(parent=self.centralwidget)
        self.them.setGeometry(QtCore.QRect(120, 210, 101, 31))
        self.them.setObjectName("them")
        self.sua = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sua.setGeometry(QtCore.QRect(120, 260, 101, 31))
        self.sua.setObjectName("sua")
        self.xoa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.xoa.setGeometry(QtCore.QRect(120, 310, 101, 31))
        self.xoa.setObjectName("xoa")
        self.luong = QtWidgets.QPushButton(parent=self.centralwidget)
        self.luong.setGeometry(QtCore.QRect(120, 360, 101, 31))
        self.luong.setObjectName("luong")
        self.thong_ke = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thong_ke.setGeometry(QtCore.QRect(120, 420, 101, 31))
        self.thong_ke.setObjectName("thong_ke")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 60, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tim_kiem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tim_kiem.setGeometry(QtCore.QRect(140, 140, 91, 23))
        self.tim_kiem.setObjectName("tim_kiem")
        self.search_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(260, 140, 321, 20))
        self.search_text.setObjectName("search_text")
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

        # Kết nối các nút với các hàm tương ứng
        self.them.clicked.connect(self.add_employee)
        self.sua.clicked.connect(self.update_employee)
        self.xoa.clicked.connect(self.delete_employee)
        self.tim_kiem.clicked.connect(self.search_employee)
        self.luong.clicked.connect(self.show_salary_details)
        self.thong_ke.clicked.connect(self.show_statistics)

        # Kết nối đến cơ sở dữ liệu
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bach2003@",
            database="NV_db"
        )
        self.cursor = self.db.cursor()

        # Hiển thị danh sách nhân viên khi khởi động
        self.display_employees()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.them.setText(_translate("MainWindow", "Thêm"))
        self.sua.setText(_translate("MainWindow", "Sửa"))
        self.xoa.setText(_translate("MainWindow", "Xóa"))
        self.luong.setText(_translate("MainWindow", "Lương"))
        self.thong_ke.setText(_translate("MainWindow", "Thống kê"))
        self.label.setText(_translate("MainWindow", "Quản lí nhân viên "))
        self.tim_kiem.setText(_translate("MainWindow", "Tìm kiếm"))

    def display_employees(self):
        self.cursor.execute("SELECT * FROM NhanVien")
        result = self.cursor.fetchall()
        display_text = ""
        for emp in result:
            display_text += f"MaNV: {emp[0]}, HoTen: {emp[1]}, PhongBan: {emp[2]}, MucLuongTheoNgay: {emp[3]}\n"
        self.plainTextEdit.setPlainText(display_text)

    def add_employee(self):
        dialog = AddEmployeeDialog()
        if dialog.exec():
            name, phong_ban, muc_luong = dialog.get_data()
            self.cursor.execute("INSERT INTO NhanVien (HoTen, PhongBan, MucLuongTheoNgay) VALUES (%s, %s, %s)",
                                (name, phong_ban, muc_luong))
            self.db.commit()
            self.display_employees()

    def update_employee(self):
        emp_id = int(self.search_text.text())
        name = "Updated Name"
        self.cursor.execute("UPDATE NhanVien SET HoTen = %s WHERE MaNV = %s", (name, emp_id))
        self.db.commit()
        self.display_employees()

    def delete_employee(self):
        emp_id = int(self.search_text.text())
        self.cursor.execute("DELETE FROM NhanVien WHERE MaNV = %s", (emp_id,))
        self.db.commit()
        self.display_employees()

    def search_employee(self):
        search_text = self.search_text.text()
        self.cursor.execute("SELECT * FROM NhanVien WHERE HoTen LIKE %s OR MaNV LIKE %s", (f"%{search_text}%", f"%{search_text}%"))
        result = self.cursor.fetchall()
        display_text = ""
        for emp in result:
            display_text += f"MaNV: {emp[0]}, HoTen: {emp[1]}, PhongBan: {emp[2]}, MucLuongTheoNgay: {emp[3]}\n"
        self.plainTextEdit.setPlainText(display_text)

    def show_salary_details(self):
        emp_id = int(self.search_text.text())
        self.cursor.execute("SELECT MucLuongTheoNgay, SoNgayCong FROM NhanVien JOIN LuongThang ON NhanVien.MaNV = LuongThang.MaNV WHERE NhanVien.MaNV = %s", (emp_id,))
        result = self.cursor.fetchall()
        if result:
            display_text = ""
            for salary, working_days in result:
                monthly_salary = salary * working_days
                display_text += f"Tháng: {result.index((salary, working_days)) + 1}, Lương tháng: {monthly_salary}\n"
            self.plainTextEdit.setPlainText(display_text)

    def show_statistics(self):
        emp_id = int(self.search_text.text())
        self.cursor.execute("SELECT MucLuongTheoNgay, SoNgayCong FROM NhanVien JOIN LuongThang ON NhanVien.MaNV = LuongThang.MaNV WHERE NhanVien.MaNV = %s", (emp_id,))
        result = self.cursor.fetchall()
        if result:
            total_salary = 0
            total_days = 0
            for salary, working_days in result:
                total_salary += salary * working_days
                total_days += working_days
            self.plainTextEdit.setPlainText(f"Thống kê cho nhân viên {emp_id}:\nTổng số ngày công: {total_days}\nTổng tiền lương trong năm: {total_salary}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
