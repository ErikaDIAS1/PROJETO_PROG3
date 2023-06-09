# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro_aeromodelo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 430)
        MainWindow.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"font:  \"Segoe UI\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_altura = QtWidgets.QLabel(self.centralwidget)
        self.label_altura.setEnabled(False)
        self.label_altura.setGeometry(QtCore.QRect(310, 270, 161, 81))
        self.label_altura.setStyleSheet("border-radius:5px;")
        self.label_altura.setText("")
        self.label_altura.setPixmap(QtGui.QPixmap("c:\\INTERFACES\\LOGO APP\\altura_do_avião-removebg-preview.png"))
        self.label_altura.setScaledContents(True)
        self.label_altura.setAlignment(QtCore.Qt.AlignCenter)
        self.label_altura.setObjectName("label_altura")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 180, 281, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutCAD_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutCAD_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayoutCAD_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayoutCAD_2.setSpacing(10)
        self.gridLayoutCAD_2.setObjectName("gridLayoutCAD_2")
        self.MembrotextEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MembrotextEdit_2.sizePolicy().hasHeightForWidth())
        self.MembrotextEdit_2.setSizePolicy(sizePolicy)
        self.MembrotextEdit_2.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.MembrotextEdit_2.setFont(font)
        self.MembrotextEdit_2.setStyleSheet("background-color: rgb(156, 156, 163);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.MembrotextEdit_2.setObjectName("MembrotextEdit_2")
        self.gridLayoutCAD_2.addWidget(self.MembrotextEdit_2, 1, 1, 1, 1)
        self.MembroLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.MembroLabel_2.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.MembroLabel_2.setFont(font)
        self.MembroLabel_2.setStyleSheet("background-color: rgb(87, 87, 94);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")
        self.MembroLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.MembroLabel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MembroLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MembroLabel_2.setIndent(1)
        self.MembroLabel_2.setObjectName("MembroLabel_2")
        self.gridLayoutCAD_2.addWidget(self.MembroLabel_2, 1, 0, 1, 1)
        self.EnvergaduraLabel_ = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.EnvergaduraLabel_.setMaximumSize(QtCore.QSize(150, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.EnvergaduraLabel_.setFont(font)
        self.EnvergaduraLabel_.setStyleSheet("background-color: rgb(87, 87, 94);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")
        self.EnvergaduraLabel_.setFrameShape(QtWidgets.QFrame.Box)
        self.EnvergaduraLabel_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EnvergaduraLabel_.setAlignment(QtCore.Qt.AlignCenter)
        self.EnvergaduraLabel_.setIndent(1)
        self.EnvergaduraLabel_.setObjectName("EnvergaduraLabel_")
        self.gridLayoutCAD_2.addWidget(self.EnvergaduraLabel_, 0, 0, 1, 1)
        self.EquipetextEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.EquipetextEdit_2.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.EquipetextEdit_2.setFont(font)
        self.EquipetextEdit_2.setStyleSheet("background-color: rgb(156, 156, 163);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.EquipetextEdit_2.setObjectName("EquipetextEdit_2")
        self.gridLayoutCAD_2.addWidget(self.EquipetextEdit_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_env = QtWidgets.QLabel(self.centralwidget)
        self.label_env.setEnabled(False)
        self.label_env.setGeometry(QtCore.QRect(310, 150, 150, 101))
        self.label_env.setMaximumSize(QtCore.QSize(150, 150))
        self.label_env.setStyleSheet("border-radius:5px;")
        self.label_env.setText("")
        self.label_env.setPixmap(QtGui.QPixmap("c:\\INTERFACES\\LOGO APP\\envergadura_do_avião-removebg-preview.png"))
        self.label_env.setScaledContents(True)
        self.label_env.setAlignment(QtCore.Qt.AlignCenter)
        self.label_env.setObjectName("label_env")
        self.label_aeromodelo = QtWidgets.QLabel(self.centralwidget)
        self.label_aeromodelo.setGeometry(QtCore.QRect(10, 10, 321, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_aeromodelo.setFont(font)
        self.label_aeromodelo.setAutoFillBackground(False)
        self.label_aeromodelo.setStyleSheet("color: rgb(87, 87, 94);\n"
"border radius: 10px;")
        self.label_aeromodelo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aeromodelo.setObjectName("label_aeromodelo")
        self.label_logo_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_logo_2.setEnabled(False)
        self.label_logo_2.setGeometry(QtCore.QRect(340, 20, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo_2.sizePolicy().hasHeightForWidth())
        self.label_logo_2.setSizePolicy(sizePolicy)
        self.label_logo_2.setText("")
        self.label_logo_2.setPixmap(QtGui.QPixmap("c:\\INTERFACES\\LOGO APP\\REQVISION_-_somente_logo-removebg-preview.png"))
        self.label_logo_2.setScaledContents(True)
        self.label_logo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo_2.setObjectName("label_logo_2")
        self.pushButton_verificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_verificar.setEnabled(False)
        self.pushButton_verificar.setGeometry(QtCore.QRect(110, 360, 259, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_verificar.setFont(font)
        self.pushButton_verificar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_verificar.setStyleSheet("background-color: rgb(87, 87, 94);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255)")
        self.pushButton_verificar.setObjectName("pushButton_verificar")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(110, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(30, 130, 71, 41))
        self.dateLabel.setMaximumSize(QtCore.QSize(150, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("background-color: rgb(87, 87, 94);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")
        self.dateLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.dateLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setIndent(1)
        self.dateLabel.setObjectName("dateLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MembroLabel_2.setText(_translate("MainWindow", "<strong>Altura"))
        self.EnvergaduraLabel_.setText(_translate("MainWindow", "<strong>Envergadura"))
        self.label_aeromodelo.setText(_translate("MainWindow", "<strong>Dimensões <br>Aeromodelo"))
        self.pushButton_verificar.setText(_translate("MainWindow", "VERIFICAR"))
        self.dateLabel.setText(_translate("MainWindow", "<strong>Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
