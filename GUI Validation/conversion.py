# EXERCICE 2

import sys
from PyQt5.QtWidgets import *

class Exercice2(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        grid = QGridLayout()
        self.templabel = QLabel("Température")
        self.entree = QLineEdit()
        self.kc = QLabel()
        self.buttconvert = QPushButton("Convertir")
        self.buttconvert.clicked.connect(self.convertir)
        self.box = QComboBox()
        self.box.activated.connect(self.choisir)
        self.box.addItem("°C -> °K")
        self.box.addItem("°K -> °C")
        self.butthelp = QPushButton("?")
        self.butthelp.clicked.connect(self.help)
        self.sortie = QLabel()
        grid.addWidget(self.templabel, 0, 0, 1, 1)
        grid.addWidget(self.entree, 0, 1, 1, 1)
        grid.addWidget(self.kc, 0, 2, 1, 1)
        grid.addWidget(self.buttconvert, 1, 1, 1, 2)
        grid.addWidget(self.box, 1, 3, 1, 1)
        grid.addWidget(self.sortie, 2, 1, 1, 2)
        grid.addWidget(self.butthelp, 3, 4, 1, 1)
        self.setLayout(grid)
        self.setWindowTitle("Deuxième exercice")

    def choisir(self):
        if self.box.currentText() == "°C -> °K":
            self.kc.setText(f"°C")
            if self.sortie.text() == "" or "Votre résultat sera en Celsus." :
                self.sortie.setText("Votre résultat sera en Kelvin.")
        else:
            self.kc.setText(f"K")
            if self.sortie.text() == "" or "Votre résultat sera en Kelvin." :
                self.sortie.setText("Votre résultat sera en Celsus.")

    def convertir(self):
        try:
            temp = float(self.entree.text())
        except ValueError:
            msg = QMessageBox()
            msg.setText("Erreur !")
            msg.setInformativeText('Vous n\'avez pas entrée une valeur correcte.')
            msg.setWindowTitle("Erreur !")
            msg.exec_()
        else:
            if self.box.currentText() == "°C -> °K":
                if temp >= -273.15:
                    resultat = temp + 273.15
                    self.sortie.setText(f"Le résultat est {resultat}K !")
                else:
                    msg = QMessageBox()
                    msg.setText("Erreur !")
                    msg.setInformativeText('Vous n\'avez pas entrée une valeur correcte.')
                    msg.setWindowTitle("Erreur !")
                    msg.exec_() 
            else:
                if temp >= 0:
                    resultat = temp - 273.15
                    resultat = resultat
                    self.sortie.setText(f"Le résultat est {resultat}°C !")
                else:
                    msg = QMessageBox()
                    msg.setText("Erreur !")
                    msg.setInformativeText('Vous n\'avez pas entrée une valeur correcte.')
                    msg.setWindowTitle("Erreur !")
                    msg.exec_()

    def help(self):
        msg = QMessageBox()
        msg.setInformativeText('Permet de convertir un nombre soit de Kelvin à Celsus, soit de Celsus à Kelvin.')
        msg.setWindowTitle('Aide')
        msg.exec_()

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
deuxiemeexo = Exercice2()
deuxiemeexo.show()

app.exec_()