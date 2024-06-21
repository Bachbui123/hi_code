import mysql.connector
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Button Add
        self.btnAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(50, 50, 100, 40))
        self.btnAdd.setObjectName("btnAdd")

        # Button Edit
        self.btnEdit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(150, 50, 100, 40))
        self.btnEdit.setObjectName("btnEdit")

        # Button Delete
        self.btnDelete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(250, 50, 100, 40))
        self.btnDelete.setObjectName("btnDelete")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.btnAdd.clicked.connect(self.add_entry)
        self.btnEdit.clicked.connect(self.edit_entry)
        self.btnDelete.clicked.connect(self.delete_entry)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Management"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="user_database"
        )

    def add_entry(self):
        dialog = UserDialog()
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            username, password = dialog.get_data()
            if username and password:
                db = self.connect_db()
                cursor = db.cursor()
                query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                db.commit()
                db.close()
                QtWidgets.QMessageBox.information(None, "Success", "New entry added.")
            else:
                QtWidgets.QMessageBox.warning(None, "Warning", "Username and password cannot be empty.")

    def edit_entry(self):
        id, ok = QtWidgets.QInputDialog.getInt(None, "Edit Entry", "Enter ID of entry to edit:")
        if ok:
            dialog = UserDialog()
            if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                new_username, new_password = dialog.get_data()
                if new_username and new_password:
                    db = self.connect_db()
                    cursor = db.cursor()
                    query = "UPDATE users SET username = %s, password = %s WHERE id = %s"
                    cursor.execute(query, (new_username, new_password, id))
                    db.commit()
                    db.close()
                    QtWidgets.QMessageBox.information(None, "Success", "Entry updated.")
                else:
                    QtWidgets.QMessageBox.warning(None, "Warning", "Username and password cannot be empty.")

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
from PyQt6 import QtCore, QtGui, QtWidgets

class UserDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("User Entry")

        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Username input
        self.username_label = QtWidgets.QLabel("Username:", self)
        self.layout.addWidget(self.username_label)
        self.username_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.username_input)

        # Password input
        self.password_label = QtWidgets.QLabel("Password:", self)
        self.layout.addWidget(self.password_label)
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        # Buttons
        self.buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel,
            self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

    def get_data(self):
        return self.username_input.text(), self.password_input.text()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
