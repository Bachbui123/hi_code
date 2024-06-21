
from PyQt6 import QtCore, QtGui, QtWidgets
import tram_may  # Assuming tram_may.py exists and contains the Ui_MainWindow class

class Ui_ManagerWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        button_style = """
        QPushButton {
            border-radius: 10px;  /* 10px radius for rounded corners */
            border: none;  /* Remove border */
            background-color: #D1D1D1;  /* Optional: background color */
        }
        QPushButton:hover {
            background-color: #A1A1A1;  /* Optional: background color on hover */
        }
        """

        # Load images
        self.home_icon = QtGui.QPixmap("img/home.png")
        self.customer_icon = QtGui.QPixmap("img/customer-satisfaction.png")
        self.stats_icon = QtGui.QPixmap("img/graph.png")
        self.logout_icon = QtGui.QPixmap("img/exit.png")  # Corrected path
        self.computer_icon = QtGui.QPixmap("img/computer.png")
        self.employee_icon = QtGui.QPixmap("img/grouping.png")
        self.service_icon = QtGui.QPixmap("img/service.png")
        self.account_icon = QtGui.QPixmap("img/management.png")  # Corrected path

        # Create a QLabel for the background image
        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background.setPixmap(QtGui.QPixmap("img/background_manager.png"))
        self.background.setScaledContents(True)

        # Create buttons
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 141, 41))
        self.pushButton.setObjectName("Trang chủ")
        self.pushButton.setIcon(QtGui.QIcon(self.home_icon))
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setStyleSheet(button_style)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 180, 141, 41))
        self.pushButton_2.setObjectName("Tài Khoản")
        self.pushButton_2.setIcon(QtGui.QIcon(self.account_icon))
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet(button_style)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 270, 141, 41))
        self.pushButton_3.setObjectName("Máy tính")
        self.pushButton_3.setIcon(QtGui.QIcon(self.computer_icon))
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet(button_style)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 360, 141, 41))
        self.pushButton_4.setObjectName("Nhân viên")
        self.pushButton_4.setIcon(QtGui.QIcon(self.employee_icon))
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setStyleSheet(button_style)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 360, 141, 41))
        self.pushButton_5.setObjectName("Thoát")
        self.pushButton_5.setIcon(QtGui.QIcon(self.logout_icon))
        self.pushButton_5.setStyleSheet(button_style)

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 90, 141, 41))
        self.pushButton_6.setObjectName("Khách hàng")
        self.pushButton_6.setIcon(QtGui.QIcon(self.customer_icon))
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setStyleSheet(button_style)

        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(580, 180, 141, 41))
        self.pushButton_7.setObjectName("Dịch vụ")
        self.pushButton_7.setIcon(QtGui.QIcon(self.service_icon))
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setStyleSheet(button_style)

        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(580, 270, 141, 41))
        self.pushButton_8.setObjectName("Thống kê")
        self.pushButton_8.setIcon(QtGui.QIcon(self.stats_icon))
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setStyleSheet(button_style)

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

        # Connect the buttons to their respective functions
        self.pushButton.clicked.connect(self.openHomePage)
        self.pushButton_2.clicked.connect(self.openTaiKhoanForm)
        self.pushButton_3.clicked.connect(self.openMayTinhForm)  # Connect to openMayTinhForm
        self.pushButton_4.clicked.connect(self.openNhanVienForm)
        self.pushButton_5.clicked.connect(MainWindow.close)  # Close the application
        self.pushButton_6.clicked.connect(self.openCustomerPage)
        self.pushButton_7.clicked.connect(self.openDichVuForm)
        self.pushButton_8.clicked.connect(self.openThongKeForm)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý quán game"))
        self.pushButton.setText(_translate("MainWindow", "Trang chủ"))
        self.pushButton_2.setText(_translate("MainWindow", "Tài Khoản"))
        self.pushButton_3.setText(_translate("MainWindow", "Máy tính"))
        self.pushButton_4.setText(_translate("MainWindow", "Nhân viên"))
        self.pushButton_5.setText(_translate("MainWindow", "Thoát"))
        self.pushButton_6.setText(_translate("MainWindow", "Khách hàng"))
        self.pushButton_7.setText(_translate("MainWindow", "Dịch vụ"))
        self.pushButton_8.setText(_translate("MainWindow", "Thống kê"))

    def openHomePage(self):
        # Code to open the home page
        pass

    def openTaiKhoanForm(self):
        # Code to open the account page form
        pass

    def openMayTinhForm(self):
        # Instantiate tram_may.Ui_MainWindow and set it up in MainWindow
        self.sub_window = QtWidgets.QMainWindow()
        self.tram_may_ui = tram_may.Ui_MainWindow()
        self.tram_may_ui.setupUi(self.sub_window)
        self.sub_window.show()

    def openNhanVienForm(self):
        # Code to open the employee form
        pass

    def openCustomerPage(self):
        # Code to open the customer page
        pass

    def openDichVuForm(self):
        # Code to open the service form
        pass

    def openThongKeForm(self):
        # Code to open the statistics form
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and initialize MainWindow for manager_system.py
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManagerWindow()
    ui.setupUi(MainWindow)
    
    # Show MainWindow for manager_system.py
    MainWindow.show()
    
    # Execute the application
    sys.exit(app.exec())