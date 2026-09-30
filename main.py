# linguagen python
# ferramenta pyside6

#inportações inicial 
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor

#cria nossa imagem visual da nossa ia 
class OrbePulsante(QWidget):

    #ele configura nosa cara da ia 
    def __init__(self):
        super().__init__()
        self.raio = 40
        self.crescendo = True
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animar)
        self.timer.start(30)

    #ela faz a animação 
    def animar(self):
        if self.crescendo:
            self.raio += 0.5
            if self.raio >= 50: self.crescendo = False
        else:
            self.raio -= 0.5
            if self.raio <= 40: self.crescendo = True
        self.update()

    # eladesenha a nossa imagem
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Fundo escuro
        painter.fillRect(self.rect(), QColor("#12121e"))
        
        cx, cy = self.width() // 2, self.height() // 2 - 30
        
        # Anéis externos
        painter.setPen(QColor("#2d285c"))
        for r in [self.raio + 20, self.raio + 40, self.raio + 60]:
            painter.drawEllipse(int(cx - r), int(cy - r), int(r * 2), int(r * 2))
            
        # Orbe roxo central
        painter.setBrush(QColor("#7c52ff"))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(int(cx - self.raio), int(cy - self.raio), int(self.raio * 2), int(self.raio * 2))


#guarda todas as defes dos botoes 
class PainelBotoes(QWidget):

    #ele cria nosso botão ele da areceita do bolo 
    def __init__(self):
        super().__init__()
        
        # Layout vertical para organizar as coisas
        layout = QVBoxLayout(self)
        
        # 1. Criação do botão "Digitar"
        self.btn_digitar = QPushButton("Digitar")
        self.btn_digitar.setMaximumSize(300, 50)
        self.btn_digitar.clicked.connect(self.mostrar_opcoes)
        
        
        # Visual do botão (roxo com pontas arredondadas)
        self.btn_digitar.setStyleSheet("""
            QPushButton {
                background-color: #7c52ff;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #683ee3;
            }
        """)
        
        # Adiciona o botão no layout
        layout.addWidget(self.btn_digitar)
        layout.setAlignment(self.btn_digitar, Qt.AlignCenter)

    #ela tira a o botaão de digitar e faz uma pergunta sobre resposta da ia 
    def mostrar_opcoes(self):
        self.btn_digitar.hide()
    
        self.lbl_pergunta = QLabel("Quer as resposta por....")
        self.layout().addWidget(self.lbl_pergunta)
    
        self.layout_botoes = QHBoxLayout()
        self.btn_texto = QPushButton("Texto")
        self.btn_audio = QPushButton("Áudio")
    
        self.layout_botoes.addWidget(self.btn_texto)
        self.layout_botoes.addWidget(self.btn_audio)
    
        self.layout().addLayout(self.layout_botoes)

# 1. É obrigatório criar o QApplication antes de qualquer widget
app = QApplication(sys.argv)


# inicializar janela 
janela = QMainWindow()
janela.setWindowTitle("IA Básica de Conversa")
janela.resize(1000, 700)
janela.setStyleSheet("background-color: #12121e;")

# Container pra juntar o Orbe + Painel em cima e embaixo
container = QWidget()
layout_principal = QVBoxLayout(container)

#ele enpilha os componente na tela 
layout_principal.addWidget(OrbePulsante())
layout_principal.addWidget(PainelBotoes())

#define o que é o conteudo principal da janela 
janela.setCentralWidget(container)

#manda a janela aparecer 
janela.show()



# 2. Adicione no final do arquivo pra manter a janela aberta:
sys.exit(app.exec())