import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    MainWindow.setEnabled(False)
    MainWindow.setGeometry(0, 0, 310, 472)
    MainWindow.setStyleSheet("background-color: rgb(227, 227, 227);")
    MainWindow.setWindowTitle("Inicio")

    centralWidget = QWidget(MainWindow)
    verticalLayout = QVBoxLayout(centralWidget)

    widget = QWidget(centralWidget)
    widget.setStyleSheet("widget{background-color: rgb(227, 227, 227);}")
    verticalLayout.addWidget(widget)

    label_bemvindo = QLabel(widget)
    label_bemvindo.setGeometry(0, 10, 291, 71)
    font = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(40)
    label_bemvindo.setFont(font)
    label_bemvindo.setAutoFillBackground(False)
    label_bemvindo.setStyleSheet("color: rgb(87, 87, 94); border-radius: 10px;")
    label_bemvindo.setText("<strong> Bem-Vindo")
    label_bemvindo.setAlignment(Qt.AlignCenter)

    label_logo = QLabel(widget)
    label_logo.setEnabled(False)
    label_logo.setGeometry(20, 100, 261, 195)
    label_logo.setText("")
    pixmap = QPixmap("c:\\INTERFACES\\LOGO APP\\REQVISION_-_somente_logo-removebg-preview.png")
    label_logo.setPixmap(pixmap)
    label_logo.setScaledContents(True)
    label_logo.setAlignment(Qt.AlignCenter)

    layoutWidget = QWidget(widget)
    layoutWidget.setGeometry(20, 320, 261, 101)
    verticalLayout_2 = QVBoxLayout(layoutWidget)

    pushButton_login = QPushButton(layoutWidget)
    pushButton_login.setEnabled(False)
    font = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(16)
    font.setWeight(50)
    font.setBold(False)
    pushButton_login.setFont(font)
    pushButton_login.setContextMenuPolicy(Qt.CustomContextMenu)
    pushButton_login.setStyleSheet("background-color: rgb(87, 87, 94); border-radius: 10px; color: rgb(255, 255, 255)")
    pushButton_login.setText("LOGIN")
    verticalLayout_2.addWidget(pushButton_login)

    pushButton_cadastro = QPushButton(layoutWidget)
    font = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(16)
    font.setWeight(50)
    font.setBold(False)
    pushButton_cadastro.setFont(font)
    pushButton_cadastro.setContextMenuPolicy(Qt.CustomContextMenu)
    pushButton_cadastro.setStyleSheet("background-color: rgb(156, 156, 163); color: rgb(87, 87, 94); border-radius: 10px;")
    pushButton_cadastro.setText("CADASTRO")
    verticalLayout_2.addWidget(pushButton_cadastro)

    MainWindow.setCentralWidget(centralWidget)
    MainWindow.setStatusBar(None)
    MainWindow.show()

    sys.exit(app.exec())
