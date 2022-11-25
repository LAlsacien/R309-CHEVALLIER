# EXERCICE 1

import sys
from PyQt5.QtWidgets import *

class Exercice1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.nom = QLabel("Saisir votre nom")
        self.champ = QLineEdit()
        self.bouton = QPushButton("Ok")
        self.bouton.clicked.connect(self.envoi)
        self.texte = QLabel()
        self.quit = QPushButton("Quitter")
        self.quit.clicked.connect(self.quitter)
        layout = QVBoxLayout()
        layout.addWidget(self.nom)
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)
        layout.addWidget(self.texte)
        layout.addWidget(self.quit)
        self.setLayout(layout)
        self.resize(300, 150)
        self.setWindowTitle("Une première fenêtre")

    def envoi(self):
        envoi = self.champ.text()
        self.texte.setText("Bonjour " + envoi + " !")
    
    def quitter(self):
        QApplication.exit(0)

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
mapremierefenetre = Exercice1()
mapremierefenetre.show()

app.exec_()

