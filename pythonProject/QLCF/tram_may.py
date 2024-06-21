
from PyQt6 import QtCore, QtGui, QtWidgets
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 50, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Background image
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background.setPixmap(QtGui.QPixmap("img/background.jpg"))
        self.background.setScaledContents(True)

        # Initialize buttons and machine states
        self.buttons = []
        self.machine_states = [False] * 13
        self.start_times = [None] * 13

        button_positions = [
            (60, 140), (210, 140), (360, 140), (510, 140), (660, 140),
            (60, 250), (210, 250), (360, 250), (510, 250), (660, 250),
            (210, 360), (360, 360), (510, 360)
        ]

        for i in range(13):
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setGeometry(QtCore.QRect(button_positions[i][0], button_positions[i][1], 121, 71))
            button.setObjectName(f"pushButton_{i+1}")
            button.setText(f"Máy {i+1}")
            button.clicked.connect(lambda checked, index=i: self.openDialog(index))
            self.buttons.append(button)

        # Exit Button
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(700, 520, 80, 40))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("Thoát")
        self.exitButton.clicked.connect(MainWindow.close)

        # Set central widget and menu/status bar
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

        # Set icons for buttons
        icon_path = "img/imgmaytinh.png"
        icon = QtGui.QIcon(icon_path)
        icon_size = QtCore.QSize(64, 64)

        for button in self.buttons:
            button.setIcon(icon)
            button.setIconSize(icon_size)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quản lý nhanh trạm máy"))

    def openDialog(self, machine_index):
        dialog = MachineDialog(machine_index, self.machine_states[machine_index], self.start_times[machine_index])
        if dialog.exec():
            self.machine_states[machine_index] = dialog.machine_state
            self.start_times[machine_index] = dialog.start_time

class MachineDialog(QtWidgets.QDialog):
    def __init__(self, machine_index, machine_state, start_time):
        super().__init__()
        self.setWindowTitle(f"Máy {machine_index + 1}")
        self.machine_index = machine_index

        self.machine_state = machine_state
        self.start_time = start_time

        layout = QtWidgets.QVBoxLayout(self)

        self.status_label = QtWidgets.QLabel()
        layout.addWidget(self.status_label)

        self.start_time_label = QtWidgets.QLabel()
        layout.addWidget(self.start_time_label)

        self.play_time_label = QtWidgets.QLabel("Số phút chơi: 0 phút")
        layout.addWidget(self.play_time_label)

        self.toggle_button = QtWidgets.QPushButton()
        self.toggle_button.clicked.connect(self.toggle_machine)
        layout.addWidget(self.toggle_button)

        self.setLayout(layout)
        self.update_ui()

    def update_ui(self):
        if self.machine_state:
            self.status_label.setText("Tình trạng: Hoạt động")
            if self.start_time:
                self.start_time_label.setText(f"Thời gian bật máy: {self.start_time.strftime('%I:%M %p')}")
            else:
                self.start_time_label.setText("Thời gian bật máy: Không xác định")
            self.toggle_button.setText("Tắt máy")
        else:
            self.status_label.setText("Tình trạng: Đã tắt")
            self.start_time_label.setText("Thời gian bật máy: N/A")
            self.play_time_label.setText("Số phút chơi: 0 phút")
            self.toggle_button.setText("Bật máy")

    def toggle_machine(self):
        self.machine_state = not self.machine_state
        if self.machine_state:
            self.start_time = datetime.datetime.now()
        else:
            self.start_time = None
        self.update_ui()

    def closeEvent(self, event):
        if self.machine_state and self.start_time:
            play_time = datetime.datetime.now() - self.start_time
            total_minutes = play_time.total_seconds() // 60
            self.play_time_label.setText(f"Số phút chơi: {int(total_minutes)} phút")
            QtWidgets.QApplication.processEvents()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())