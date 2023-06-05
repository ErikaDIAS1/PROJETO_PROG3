import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inicio(object):
    def setupUi(self, inicio):
        inicio.setObjectName("inicio")
        inicio.resize(541, 390)
        inicio.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon.fromTheme("REQVISION")
        inicio.setWindowIcon(icon)

        self.progressBar = QtWidgets.QProgressBar(inicio)
        self.progressBar.setGeometry(QtCore.QRect(30, 360, 481, 20))
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                        "border-radius:10px;\n"
                                        "background-color:#e3e3e3\n"
                                        "}\n"
                                        "\n"
                                        "QProgressBar::chunk{\n"
                                        "border-radius:10px;\n"
                                        "background-color:#57575e\n"
                                        "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.label = QtWidgets.QLabel(inicio)
        self.label.setGeometry(QtCore.QRect(0, -30, 549, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\INTERFACES\\LOGO APP\\REQVISION.bmp"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.raise_()
        self.progressBar.raise_()

        self.retranslateUi(inicio)
        QtCore.QMetaObject.connectSlotsByName(inicio)

    def retranslateUi(self, inicio):
        _translate = QtCore.QCoreApplication.translate
        inicio.setWindowTitle(_translate("inicio", "Splash Screen"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inicio = QtWidgets.QMainWindow()
    ui = Ui_inicio()
    ui.setupUi(inicio)

    inicio.show()

    # Atualizar valor da barra de progresso com delay
    progress_value = 0

    def update_progress():
        global progress_value
        ui.progressBar.setValue(progress_value)
        progress_value += 1

        if progress_value > 100:
            timer.stop()

    timer = QtCore.QTimer()
    timer.timeout.connect(update_progress)
    timer.start(100)  # Atraso de 100 ms (0.1 segundos)

    sys.exit(app.exec_())
