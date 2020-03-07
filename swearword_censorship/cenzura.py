# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import textwrap


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 557)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEditNadajnik = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditNadajnik.setGeometry(QtCore.QRect(10, 30, 300, 200))
        self.textEditNadajnik.setObjectName("textEditNadajnik")

        self.buttonBinaryzacja = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBinaryzacja.setGeometry(QtCore.QRect(90, 230, 151, 40))
        self.buttonBinaryzacja.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBinaryzacja.setAutoFillBackground(False)
        self.buttonBinaryzacja.setIconSize(QtCore.QSize(16, 16))
        self.buttonBinaryzacja.setObjectName("buttonBinaryzacja")
        self.buttonBinaryzacja.clicked.connect(self.na_binarny)

        self.buttonZapisz = QtWidgets.QPushButton(self.centralwidget)
        self.buttonZapisz.setGeometry(QtCore.QRect(90, 470, 151, 40))
        self.buttonZapisz.setObjectName("buttonZapisz")
        self.buttonZapisz.clicked.connect(self.zapisz)

        self.buttonOdczytaj = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOdczytaj.setGeometry(QtCore.QRect(410, 230, 151, 40))
        self.buttonOdczytaj.setObjectName("buttonOdczytaj")
        self.buttonOdczytaj.clicked.connect(self.odczytaj)

        self.buttonTekst = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTekst.setGeometry(QtCore.QRect(410, 470, 151, 40))
        self.buttonTekst.setObjectName("buttonTekst")
        self.buttonTekst.clicked.connect(self.na_polski)

        self.labelNadajnik = QtWidgets.QLabel(self.centralwidget)
        self.labelNadajnik.setEnabled(True)
        self.labelNadajnik.setGeometry(QtCore.QRect(20, 10, 301, 20))
        self.labelNadajnik.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelNadajnik.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNadajnik.setObjectName("labelNadajnik")

        self.labelOdbiornik = QtWidgets.QLabel(self.centralwidget)
        self.labelOdbiornik.setGeometry(QtCore.QRect(330, 10, 301, 16))
        self.labelOdbiornik.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOdbiornik.setObjectName("labelOdbiornik")

        self.textEditOdbiornik = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditOdbiornik.setGeometry(QtCore.QRect(330, 270, 300, 200))
        self.textEditOdbiornik.setObjectName("textEditOdbiornik")

        self.textEditNadajnikBinarny = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditNadajnikBinarny.setGeometry(QtCore.QRect(10, 270, 300, 200))
        self.textEditNadajnikBinarny.setObjectName("textEditNadajnikBinarny")

        self.textEditOdbiornikBinarny = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditOdbiornikBinarny.setGeometry(QtCore.QRect(330, 30, 300, 200))
        self.textEditOdbiornikBinarny.setObjectName("textEditOdbiornikBinarny")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RS232"))
        self.buttonZapisz.setText(_translate("MainWindow", "Zapisz"))
        self.buttonOdczytaj.setText(_translate("MainWindow", "Odczytaj"))
        self.labelNadajnik.setText(_translate("MainWindow", "Nadajnik"))
        self.labelOdbiornik.setText(_translate("MainWindow", "Odbiornik"))
        self.buttonBinaryzacja.setText(_translate("MainWindow", "Tłumacz na binarny"))
        self.buttonTekst.setText(_translate("MainWindow", "Tłumacz na polski"))

    def na_binarny(self):
        input = self.textEditNadajnik.toPlainText()
        binary = []
        for char in input:
            char = format(ord(char), 'b') # zamiana znaku na binarny odpowiednik
            char = char.zfill(8) # uzupełnienie do 8 zerami z przodu
            char = char[::-1] # odwrócenie ciągu bitów, aby były od LSB do MSB
            binary.append(str("0") + char + str("11")) # dodanie bitu startu, znaku oraz bitów stopu
        print("binary\n", binary)
        binary_string = "".join(binary)
        print("binary string\n" + binary_string)
        self.textEditNadajnikBinarny.setText(binary_string)
        self.textEditNadajnikBinarny.repaint()

    def zapisz(self):
        input = self.textEditNadajnikBinarny.toPlainText()
        with open("text.txt", "w") as input_file:
            input_file.write(input)

    def odczytaj(self):
        with open("text.txt", "r") as output_file:
            text = output_file.read()
        print("odczytany\n" + text)
        self.textEditOdbiornikBinarny.setText(text)
        self.textEditOdbiornikBinarny.repaint()

    def na_polski(self):
        final_output = []
        with open("text.txt", "r") as output_file:
            text = output_file.read()
        letter_list = []
        letters = textwrap.wrap(text, 11) # podzielenie łańcucha na pojedyncze znaki
        for letter in letters:
            letter = letter[1:8] # odrzucenie bitów start/stop
            letter = letter[::-1] # odwrócenie ciągu bitów, aby były od MSB do LSB
            letter = int(letter, 2)
            letter = chr(letter) # zamiana ciągu bitów na  odpowiadający znak ASCII
            letter_list.append(letter)
        output = "".join(letter_list)
        words = output.split()
        with open("grubianstwa.txt", "r") as grub_file: # wczytanie grubiaństw z pliku tekstowego
            grubianstwa = grub_file.read()
        for word in words:  # porównanie słów z wiadomości z grubiaństwami w celu ich odnalezienia
            if word in grubianstwa:
                word = "*"*len(word)    # cenzura odnalezionych grubiaństw
                final_output.append(word)
            else:
                final_output.append(word)
        final_output = " ".join(final_output)
        self.textEditOdbiornik.setText(final_output)
        self.textEditOdbiornik.repaint()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())