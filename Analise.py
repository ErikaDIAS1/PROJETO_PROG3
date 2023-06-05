from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class RelatorioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatório")
        self.setGeometry(0, 0, 581, 500)
        self.setMaximumSize(16777215, 500)
        self.setStyleSheet("background-color: rgb(227, 227, 227);")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)
        grid_layout.setContentsMargins(10, 10, 10, 10)
        grid_layout.setSpacing(10)

        label_relatorio = QLabel("<strong>Relatório de Aprovação", self)
        label_relatorio.setGeometry(10, 10, 451, 71)
        label_relatorio.setFont(QFont("Segoe UI", 30))
        label_relatorio.setStyleSheet("color: rgb(87, 87, 94); border-radius: 10px;")
        label_relatorio.setAutoFillBackground(False)
        label_relatorio.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_relatorio, 0, 0, 1, 2)

        label_equipe = QLabel("Nome da Equipe", self)
        label_equipe.setMaximumSize(150, 45)
        label_equipe.setFont(QFont("Segoe UI", 12, 75, True))
        label_equipe.setStyleSheet("background-color: rgb(87, 87, 94); border-radius: 10px; color: rgb(255, 255, 255);")
        label_equipe.setFrameShape(QLabel.NoFrame)
        label_equipe.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_equipe, 1, 0)

        label_equipe2 = QLabel(self)
        label_equipe2.setMaximumSize(350, 45)
        label_equipe2.setFont(QFont("Segoe UI", 12, 75, True))
        label_equipe2.setStyleSheet("background-color: rgb(174, 174, 181); border-radius: 10px; color: rgb(87, 87, 94);")
        label_equipe2.setFrameShape(QLabel.NoFrame)
        label_equipe2.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_equipe2, 1, 1)

        label_status = QLabel(self)
        label_status.setMaximumSize(350, 45)
        label_status.setFont(QFont("Segoe UI", 12, 75, True))
        label_status.setStyleSheet("background-color: rgb(174, 174, 181); border-radius: 10px; color: rgb(87, 87, 94);")
        label_status.setFrameShape(QLabel.NoFrame)
        label_status.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_status, 2, 1)

        label_stts = QLabel("Status", self)
        label_stts.setMaximumSize(150, 45)
        label_stts.setFont(QFont("Segoe UI", 12, 75, True))
        label_stts.setStyleSheet("background-color: rgb(87, 87, 94); border-radius: 10px; color: rgb(255, 255, 255);")
        label_stts.setFrameShape(QLabel.NoFrame)
        label_stts.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_stts, 2, 0)

        label_logo = QLabel(self)
        label_logo.setEnabled(False)
        label_logo.setGeometry(490, 10, 61, 53)  # Alterado o tamanho do logo
        label_logo.setText("")
        label_logo.setPixmap(QPixmap("c:\\INTERFACES\\LOGO APP\\REQVISION_-_somente_logo-removebg-preview.png").scaled(61, 53, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation))
        label_logo.setScaledContents(True)
        label_logo.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_logo, 0, 2)

        label_aprov = QLabel(self)
        label_aprov.setGeometry(10, 250, 561, 231)
        label_aprov.setMaximumSize(1500, 1500)
        label_aprov.setFont(QFont("Segoe UI", 12, 50, False))
        label_aprov.setStyleSheet("background-color: rgb(87, 87, 94); border-radius: 10px; color: rgb(255, 255, 255);"
                                  "padding: 10px;")  # Adicionado espaçamento nas bordas
        label_aprov.setFrameShape(QLabel.NoFrame)
        label_aprov.setText("<html><head/><body><p>O projeto em questão está de acordo com as restrições <br>geométricas estabelecidas no regulamento da SAE Brasil Aerodesign <br>seção 7 - Restrições Geométricas. <br>De acordo com o regulamento, a aeronave em Configuração deve <br>atender às seguintes dimensões: </p><p><br>Sd = H + B ≤ 2.9m</p><p>H ≤ 0.6m</p></body></html> <strong> Neste caso, não são necessárias alterações.")
        label_aprov.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        grid_layout.addWidget(label_aprov, 3, 0, 1, 3)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    relatorio_window = RelatorioWindow()
    relatorio_window.show()
    sys.exit(app.exec_())

