import mysql.connector
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 100, 311, 41))
        self.textEdit.setObjectName("textEdit")

        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 190, 481, 221))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 450, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 450, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.new_entry)
        self.pushButton_3.clicked.connect(self.delete_entry)

        self.apply_styles()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Management"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "New"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bach2003@",
            database="user_database"
        )
#search form
    def search(self):
        # Lấy cụm từ tìm kiếm từ textEdit và loại bỏ khoảng trắng đầu/cuối
        search_term = self.textEdit.toPlainText().strip()
        
        # Kiểm tra nếu cụm từ tìm kiếm trống, hiển thị thông báo cảnh báo
        if not search_term:
            QtWidgets.QMessageBox.warning(None, "Warning", "Please enter a search term.")
            return
        
        # Kết nối đến cơ sở dữ liệu
        db = self.connect_db()
        cursor = db.cursor()

        # Kiểm tra nếu cụm từ tìm kiếm là "all" (không phân biệt chữ hoa chữ thường)
        if search_term.lower() == "all":
            query = "SELECT * FROM users"
            cursor.execute(query)
        else:
            # Tìm kiếm theo username với điều kiện LIKE (có chứa cụm từ tìm kiếm)
            query = "SELECT * FROM users WHERE username LIKE %s"
            cursor.execute(query, ('%' + search_term + '%',))
        
        # Lấy tất cả kết quả từ truy vấn
        results = cursor.fetchall()
        
        # Đóng kết nối đến cơ sở dữ liệu
        db.close()

        # Kiểm tra nếu có kết quả
        if results:
            # Tạo chuỗi kết quả từ các hàng trong kết quả truy vấn
            result_text = '\n'.join([f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}" for row in results])
        else:
            # Nếu không có kết quả, hiển thị thông báo không tìm thấy kết quả
            result_text = "No results found."
        
        # Hiển thị chuỗi kết quả trong textBrowser
        self.textBrowser.setText(result_text)


    def new_entry(self):
        username, ok = QtWidgets.QInputDialog.getText(None, "New Entry", "Enter username:")
        if ok and username:
            password, ok = QtWidgets.QInputDialog.getText(None, "New Entry", "Enter password:", QtWidgets.QLineEdit.EchoMode.Password)
            if ok and password:
                db = self.connect_db()
                cursor = db.cursor()
                query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                db.commit()
                db.close()
                QtWidgets.QMessageBox.information(None, "Success", "New entry added.")
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "Password cannot be empty.")
        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "Username cannot be empty.")

    def delete_entry(self):
        id, ok = QtWidgets.QInputDialog.getInt(None, "Delete Entry", "Enter ID of entry to delete:")
        if ok:
            db = self.connect_db()
            cursor = db.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            db.commit()
            db.close()
            if cursor.rowcount > 0:
                QtWidgets.QMessageBox.information(None, "Success", "Entry deleted.")
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "No entry with that ID.")

    def apply_styles(self):
        self.centralwidget.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
                border: none;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTextEdit, QTextBrowser {
                border: 2px solid #d3d3d3;
                border-radius: 10px;
                padding: 10px;
                background-color: #ffffff;
            }
        """)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
 