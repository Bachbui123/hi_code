from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.them = QtWidgets.QPushButton(parent=self.centralwidget)
        self.them.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.them.setObjectName("them")
        self.sua = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sua.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.sua.setObjectName("sua")
        self.xoa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.xoa.setGeometry(QtCore.QRect(190, 220, 75, 23))
        self.xoa.setObjectName("xoa")
        self.danhsach = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.danhsach.setGeometry(QtCore.QRect(340, 120, 351, 192))
        self.danhsach.setObjectName("danhsach")
        self.danhsach.setColumnCount(3)
        self.danhsach.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.danhsach.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.danhsach.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.danhsach.setHorizontalHeaderItem(2, item)
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

        # Sự kiện click vào button
        self.them.clicked.connect(self.add)
        self.sua.clicked.connect(self.edit)
        self.xoa.clicked.connect(self.delete)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.them.setText(_translate("MainWindow", "Thêm"))
        self.sua.setText(_translate("MainWindow", "Sửa"))
        self.xoa.setText(_translate("MainWindow", "Xóa"))
        item = self.danhsach.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã NV"))
        item = self.danhsach.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.danhsach.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lương"))

    def connect_db(self):
        return mysql.connector.connect(
            host='localhost',
            username='root',
            password='Bach2003@',
            database='ql_nv'
        )

    def add(self):
    # Tạo đối tượng hộp thoại nhập liệu
        dialog = UserDialog()
    
    # Hiển thị hộp thoại và kiểm tra xem người dùng đã nhấn nút Ok hay chưa
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        # Lấy dữ liệu người dùng nhập từ hộp thoại
            id, name, salary = dialog.get_data()
        
        # Kiểm tra xem người dùng đã nhập đầy đủ tên và lương hay chưa
        if name and salary:
            try:
                # Kết nối tới cơ sở dữ liệu
                db = self.connect_db()
                cursor = db.cursor()
                
                # Chuẩn bị câu lệnh SQL để chèn dữ liệu vào bảng employees
                query = "INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)"
                
                # Thực thi câu lệnh SQL với các giá trị id, name, salary
                cursor.execute(query, (id, name, salary))
                
                # Commit giao dịch để lưu các thay đổi vào cơ sở dữ liệu
                db.commit()
                
                # Đóng kết nối cơ sở dữ liệu
                db.close()
                
                # Hiển thị thông báo thành công cho người dùng
                QtWidgets.QMessageBox.information(None, "Success", "New entry added.")
                
                # Tải lại dữ liệu từ cơ sở dữ liệu và hiển thị lên bảng
                self.load_data()
            except mysql.connector.Error as err:
                # Nếu có lỗi xảy ra trong quá trình thêm dữ liệu, hiển thị thông báo lỗi
                QtWidgets.QMessageBox.critical(None, "Error", f"Error: {err}")
        else:
            # Nếu tên hoặc lương bị bỏ trống, hiển thị cảnh báo cho người dùng
            QtWidgets.QMessageBox.warning(None, "Warning", "Name and salary cannot be empty.")

    def edit(self):
    # Lấy chỉ số hàng hiện tại mà người dùng chọn trong bảng
        row = self.danhsach.currentRow()
    
    # Kiểm tra xem có hàng nào được chọn không
        if row >= 0:
        # Lấy mã nhân viên từ hàng được chọn
            id_item = self.danhsach.item(row, 0)
        
        # Kiểm tra xem có mã nhân viên trong hàng được chọn không
        if id_item:
            # Chuyển mã nhân viên từ dạng văn bản sang số nguyên
            id = int(id_item.text())
            
            # Tạo đối tượng hộp thoại nhập liệu để chỉnh sửa thông tin
            dialog = UserDialog()
            
            # Hiển thị hộp thoại và kiểm tra xem người dùng đã nhấn nút Ok hay chưa
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                # Lấy dữ liệu mới từ hộp thoại
                new_id, new_name, new_salary = dialog.get_data()
                
                # Kiểm tra xem tên mới và lương mới có được nhập đầy đủ không
                if new_name and new_salary:
                    try:
                        # Kết nối tới cơ sở dữ liệu
                        db = self.connect_db()
                        cursor = db.cursor()
                        
                        # Chuẩn bị câu lệnh SQL để cập nhật thông tin nhân viên
                        query = "UPDATE employees SET name = %s, salary = %s WHERE id = %s"
                        
                        # Thực thi câu lệnh SQL với các giá trị mới
                        cursor.execute(query, (new_name, new_salary, new_id))
                        
                        # Commit giao dịch để lưu các thay đổi vào cơ sở dữ liệu
                        db.commit()
                        
                        # Đóng kết nối cơ sở dữ liệu
                        db.close()
                        
                        # Hiển thị thông báo thành công cho người dùng
                        QtWidgets.QMessageBox.information(None, "Success", "Entry updated.")
                        
                        # Tải lại dữ liệu từ cơ sở dữ liệu và hiển thị lên bảng
                        self.load_data()
                    except mysql.connector.Error as err:
                        # Nếu có lỗi xảy ra trong quá trình cập nhật dữ liệu, hiển thị thông báo lỗi
                        QtWidgets.QMessageBox.critical(None, "Error", f"Error: {err}")
                else:
                    # Nếu tên mới hoặc lương mới bị bỏ trống, hiển thị cảnh báo cho người dùng
                    QtWidgets.QMessageBox.warning(None, "Warning", "Name and salary cannot be empty.")
        else:
        # Nếu không có hàng nào được chọn, hiển thị cảnh báo cho người dùng
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a row to edit.")


    def delete(self):
    # Lấy chỉ số hàng hiện tại mà người dùng chọn trong bảng
        row = self.danhsach.currentRow()
    
    # Kiểm tra xem có hàng nào được chọn không
        if row >= 0:
        # Lấy mã nhân viên từ hàng được chọn
            id_item = self.danhsach.item(row, 0)
        
        # Kiểm tra xem có mã nhân viên trong hàng được chọn không
        if id_item:
            # Chuyển mã nhân viên từ dạng văn bản sang số nguyên
            id = int(id_item.text())
            try:
                # Kết nối tới cơ sở dữ liệu
                db = self.connect_db()
                cursor = db.cursor()
                
                # Chuẩn bị câu lệnh SQL để xóa nhân viên
                query = "DELETE FROM employees WHERE id = %s"
                
                # Thực thi câu lệnh SQL với mã nhân viên
                cursor.execute(query, (id,))
                
                # Commit giao dịch để lưu các thay đổi vào cơ sở dữ liệu
                db.commit()
                
                # Đóng kết nối cơ sở dữ liệu
                db.close()
                
                # Kiểm tra xem có hàng nào bị ảnh hưởng (xóa thành công)
                if cursor.rowcount > 0:
                    # Hiển thị thông báo thành công cho người dùng
                    QtWidgets.QMessageBox.information(None, "Success", "Entry deleted.")
                    
                    # Tải lại dữ liệu từ cơ sở dữ liệu và hiển thị lên bảng
                    self.load_data()
                else:
                    # Hiển thị cảnh báo nếu không có mục nào với mã nhân viên đó
                    QtWidgets.QMessageBox.warning(None, "Warning", "No entry with that ID.")
            except mysql.connector.Error as err:
                # Nếu có lỗi xảy ra trong quá trình xóa dữ liệu, hiển thị thông báo lỗi
                QtWidgets.QMessageBox.critical(None, "Error", f"Error: {err}")
        else:
        # Nếu không có hàng nào được chọn, hiển thị cảnh báo cho người dùng
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select a row to delete.")

    
    def load_data(self):
    # Kết nối tới cơ sở dữ liệu
        db = self.connect_db()
        cursor = db.cursor()
        
        # Chuẩn bị câu lệnh SQL để lấy tất cả dữ liệu từ bảng 'employees'
        query = "SELECT * FROM employees"
        
        # Thực thi câu lệnh SQL
        cursor.execute(query)
        
        # Lấy tất cả các kết quả từ câu lệnh SQL
        results = cursor.fetchall()
        
        # Đóng kết nối cơ sở dữ liệu
        db.close()

        # Đặt lại số hàng của bảng 'danhsach' về 0 để xóa dữ liệu cũ
        self.danhsach.setRowCount(0)
        
        # Duyệt qua từng hàng dữ liệu trong kết quả
        for row_number, row_data in enumerate(results):
            # Thêm một hàng mới vào bảng 'danhsach'
            self.danhsach.insertRow(row_number)
            
            # Duyệt qua từng cột trong hàng dữ liệu
            for column_number, data in enumerate(row_data):
                # Đặt dữ liệu vào ô tương ứng trong bảng 'danhsach'
                self.danhsach.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


class UserDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # Gọi hàm khởi tạo của lớp cha QtWidgets.QDialog
        super().__init__(parent)
        
        # Đặt tiêu đề cho cửa sổ dialog
        self.setWindowTitle("User Entry")

        # Tạo layout chính cho dialog
        self.layout = QtWidgets.QVBoxLayout(self)

        # Tạo và thêm nhãn và ô nhập liệu cho "Mã NV"
        self.id_label = QtWidgets.QLabel("Mã NV:", self)
        self.layout.addWidget(self.id_label)
        self.id_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.id_input)

        # Tạo và thêm nhãn và ô nhập liệu cho "Họ tên"
        self.name_label = QtWidgets.QLabel("Họ tên:", self)
        self.layout.addWidget(self.name_label)
        self.name_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.name_input)

        # Tạo và thêm nhãn và ô nhập liệu cho "Lương"
        self.salary_label = QtWidgets.QLabel("Lương:", self)
        self.layout.addWidget(self.salary_label)
        self.salary_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.salary_input)

        # Tạo và thêm nút Ok và Cancel vào dialog
        self.buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel,
            self)
        
        # Kết nối tín hiệu chấp nhận với phương thức accept (khi nhấn Ok)
        self.buttons.accepted.connect(self.accept)
        
        # Kết nối tín hiệu từ chối với phương thức reject (khi nhấn Cancel)
        self.buttons.rejected.connect(self.reject)
        
        # Thêm nút vào layout
        self.layout.addWidget(self.buttons)

    # Phương thức lấy dữ liệu từ các ô nhập liệu
    def get_data(self):
        # Trả về dữ liệu nhập vào từ các ô: id, name, và salary
        return self.id_input.text(), self.name_input.text(), self.salary_input.text()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.load_data()  # Load data when the application starts
    MainWindow.show()
    sys.exit(app.exec())
