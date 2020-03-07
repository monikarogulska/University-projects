# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSound
import time
import random
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    opt_wyniki = []
    akus_wyniki = []
    szkol_opt = 2
    szkol_akus = 2
    test_opt = 2
    test_akus = 2
    czas_opt = 0
    czas_akus = 0

    def __init__(self):
        self.i = 1
        self.j = 1
        self.i_test = 1
        self.j_test = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # WYJŚCIE

        self.button_quit = QtWidgets.QPushButton(self.centralwidget)
        self.button_quit.setGeometry(QtCore.QRect(5, 10, 890, 32))
        self.button_quit.setObjectName("button_quit")
        self.button_quit.setStyleSheet("background-color: #ff3b00")
        self.button_quit.clicked.connect(QApplication.instance().quit)

        # LABELS

        self.label_opt = QtWidgets.QLabel(self.centralwidget)
        self.label_opt.setGeometry(QtCore.QRect(0, 60, 450, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_opt.setFont(font)
        self.label_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_opt.setObjectName("label_opt")
        self.label_akus = QtWidgets.QLabel(self.centralwidget)
        self.label_akus.setGeometry(QtCore.QRect(450, 60, 450, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_akus.setFont(font)
        self.label_akus.setAlignment(QtCore.Qt.AlignCenter)
        self.label_akus.setObjectName("label_akus")

        # ZASADY

        self.button_zasady_opt = QtWidgets.QPushButton(self.centralwidget)
        self.button_zasady_opt.setGeometry(QtCore.QRect(25, 100, 411, 41))
        self.button_zasady_opt.setStyleSheet("background-color: #fffa00")
        self.button_zasady_opt.setObjectName("button_zasady_opt")
        self.button_zasady_opt.clicked.connect(self.zasady_opt)

        self.button_zasady_akus = QtWidgets.QPushButton(self.centralwidget)
        self.button_zasady_akus.setGeometry(QtCore.QRect(484, 100, 391, 41))
        self.button_zasady_akus.setStyleSheet("background-color: #fffa00")
        self.button_zasady_akus.setObjectName("button_zasady_akus")
        self.button_zasady_akus.clicked.connect(self.zasady_akus)

        # MAIN

        self.button_sygnalizacja = QtWidgets.QPushButton(self.centralwidget)
        self.button_sygnalizacja.setGeometry(QtCore.QRect(130, 300, 190, 190))
        self.button_sygnalizacja.setObjectName("button_sygnalizacja")
        self.button_sygnalizacja.setIcon(QtGui.QIcon("lights.png"))
        self.button_sygnalizacja.setIconSize(QtCore.QSize(170, 170))
        self.button_sygnalizacja.clicked.connect(self.time_stop_opt)

        self.button_glosnik = QtWidgets.QPushButton(self.centralwidget)
        self.button_glosnik.setGeometry(QtCore.QRect(580, 300, 190, 190))
        self.button_glosnik.setObjectName("button_glosnik")
        self.button_glosnik.setIcon(QtGui.QIcon("glosnik.png"))
        self.button_glosnik.setIconSize(QtCore.QSize(170, 170))
        self.button_glosnik.clicked.connect(self.time_stop_akus)


        # WYNIKI

        self.button_wyniki_opt = QtWidgets.QPushButton(self.centralwidget)
        self.button_wyniki_opt.setGeometry(QtCore.QRect(25, 625, 411, 41))
        self.button_wyniki_opt.setObjectName("button_wyniki_opt")
        self.button_wyniki_opt.setStyleSheet("background-color: #00cbff")
        self.button_wyniki_opt.clicked.connect(self.wyniki_opt)

        self.button_wyniki_akus = QtWidgets.QPushButton(self.centralwidget)
        self.button_wyniki_akus.setGeometry(QtCore.QRect(484, 625, 391, 41))
        self.button_wyniki_akus.setObjectName("button_wyniki_akus")
        self.button_wyniki_akus.setStyleSheet("background-color: #00cbff")
        self.button_wyniki_akus.clicked.connect(self.wyniki_akus)

        #

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 50, 20, 631))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 40, 901, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        # WYNIKI

        self.textEdit_opt = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_opt.setGeometry(QtCore.QRect(25, 500, 411, 120))
        self.textEdit_opt.setObjectName("textEdit_opt")
        self.textEdit_opt.setReadOnly(True)

        self.textEdit_akus = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_akus.setGeometry(QtCore.QRect(484, 500, 391, 120))
        self.textEdit_akus.setObjectName("textEdit_akus")
        self.textEdit_akus.setReadOnly(True)

        # START

        self.button_start_opt = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_opt.setGeometry(QtCore.QRect(25, 140, 411, 41))
        self.button_start_opt.setObjectName("button_start_opt")
        self.button_start_opt.setStyleSheet("background-color: #f48c04")
        self.button_start_opt.clicked.connect(self.start_opt)

        self.button_start_akus = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_akus.setGeometry(QtCore.QRect(484, 140, 391, 41))
        self.button_start_akus.setObjectName("button_start_akus")
        self.button_start_akus.setStyleSheet("background-color: #f48c04")
        self.button_start_akus.clicked.connect(self.start_akus)

        # INFO

        self.textEdit_info_opt = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_info_opt.setGeometry(QtCore.QRect(25, 190, 411, 100))
        self.textEdit_info_opt.setObjectName("textEdit_info_opt")
        self.textEdit_info_opt.setReadOnly(True)

        self.textEdit_info_akus = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_info_akus.setGeometry(QtCore.QRect(484, 190, 391, 100))
        self.textEdit_info_akus.setObjectName("textEdit_info_akus")
        self.textEdit_info_akus.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test na czas reakcji"))
        self.button_quit.setText(_translate("MainWindow", "Wyjście"))
        self.label_opt.setText(_translate("MainWindow", "Bodźce optyczne"))
        self.label_akus.setText(_translate("MainWindow", "Bodźce akustyczne"))
        self.button_zasady_opt.setText(_translate("MainWindow", "Zasady"))
        self.button_zasady_akus.setText(_translate("MainWindow", "Zasady"))
        self.button_sygnalizacja.setText(_translate("MainWindow", ""))
        self.button_glosnik.setText(_translate("MainWindow", ""))
        self.button_wyniki_opt.setText(_translate("MainWindow", "Wyniki"))
        self.button_wyniki_akus.setText(_translate("MainWindow", "Wyniki"))
        self.button_start_opt.setText(_translate("MainWindow", "Start"))
        self.button_start_akus.setText(_translate("MainWindow", "Start"))

    def zasady_opt(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Test optyczny")
        msg.setInformativeText("Test zaczyna się fazą szkoleniową, w której użytkownik ma 3 próby. "
                               "Następnie automatycznie włącza się główny test składający się z 5 prób, których czasy są mierzone "
                               "i wyświetlane w oknie pod przyciskiem. Przycisk naciskamy, gdy zmieni on swój kolor.")
        msg.exec_()

    def zasady_akus(self):
        msg_a = QMessageBox()
        msg_a.setIcon(QMessageBox.Information)
        msg_a.setText("Test optyczny")
        msg_a.setInformativeText("Test zaczyna się fazą szkoleniową, w której użytkownik ma 3 próby. "
                               "Następnie automatycznie włącza się główny test składający się z 5 prób, których czasy są mierzone "
                               "i wyświetlane w oknie pod przyciskiem. Przycisk naciskamy, gdy usłyszymy dźwięk.")
        msg_a.exec_()

    def start_opt(self):
        green = QtGui.QColor(0, 255, 0)
        white = QtGui.QColor(255, 255, 255)
        red = QtGui.QColor(255, 0, 0)
        font = QtGui.QFont()
        font.setPointSize(40)
        font_small = QtGui.QFont()
        font_small.setPointSize(35)
        for i in range(self.szkol_opt):
            self.textEdit_info_opt.setTextBackgroundColor(white) # ustawienie białego tła
            self.textEdit_info_opt.setText("FAZA SZKOLENIOWA") # ustawienie tekstu w polu textEdit
            self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter) # wyśrodkowanie
            self.textEdit_info_opt.setFont(font) # ustawienie zdefiniowanej wcześniej czcionki
            self.textEdit_info_opt.repaint() # odświeżenie
            delay = random.randrange(2000, 4000) # losowanie czasu po którym zapali się zielone okienko
            QtTest.QTest.qWait(delay)
            self.time_start_opt() # pobranie czasu systemowego
            self.textEdit_info_opt.setTextBackgroundColor(green) # ustawienie zielonego koloru
            self.textEdit_info_opt.setText("FAZA SZKOLENIOWA")
            self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
            self.textEdit_info_opt.setFont(font)
            self.textEdit_info_opt.repaint()
            QtTest.QTest.qWait(2000)
        self.textEdit_info_opt.setTextBackgroundColor(red)
        self.textEdit_info_opt.setText("KONIEC FAZY SZKOLENIOWEJ")
        self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_opt.setFont(font_small)
        self.textEdit_info_opt.repaint()
        QtTest.QTest.qWait(2000)
        self.textEdit_info_opt.setTextBackgroundColor(white)
        self.textEdit_info_opt.setText("CZAS NA TEST")
        self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_opt.setFont(font)
        self.textEdit_info_opt.repaint()
        QtTest.QTest.qWait(2000)
        for i in range(self.test_opt):
            self.textEdit_info_opt.setTextBackgroundColor(white)
            self.textEdit_info_opt.setText("TEST")
            self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
            self.textEdit_info_opt.setFont(font)
            self.textEdit_info_opt.repaint()
            delay = random.randrange(2000, 4000)
            QtTest.QTest.qWait(delay)
            self.time_start_opt()
            self.textEdit_info_opt.setTextBackgroundColor(green)
            self.textEdit_info_opt.setText("TEST")
            self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
            self.textEdit_info_opt.setFont(font)
            self.textEdit_info_opt.repaint()
            QtTest.QTest.qWait(2000)
        self.textEdit_info_opt.setTextBackgroundColor(red)
        self.textEdit_info_opt.setText("KONIEC TESTU")
        self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_opt.setFont(font)
        self.textEdit_info_opt.repaint()
        QtTest.QTest.qWait(2000)
        self.textEdit_info_opt.setTextBackgroundColor(white)
        self.textEdit_info_opt.setText("ZOBACZ WYNIKI")
        self.textEdit_info_opt.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_opt.setFont(font)
        self.textEdit_info_opt.repaint()

    def start_akus(self):
        font = QtGui.QFont()
        font.setPointSize(40)
        font_small = QtGui.QFont()
        font_small.setPointSize(35)
        red = QtGui.QColor(255, 0, 0)
        white = QtGui.QColor(255, 255, 255)
        for i in range(self.szkol_akus):
            self.textEdit_info_akus.setText("FAZA SZKOLENIOWA")
            self.textEdit_info_akus.setAlignment(QtCore.Qt.AlignCenter)
            self.textEdit_info_akus.setFont(font)
            self.textEdit_info_akus.repaint()
            delay = random.randrange(2000, 4000)
            QtTest.QTest.qWait(delay)
            self.time_start_akus()
            QSound.play("laser-01.wav")
            self.textEdit_akus.repaint()
            QtTest.QTest.qWait(2000)
        self.textEdit_info_akus.setTextBackgroundColor(red)
        self.textEdit_info_akus.setText("KONIEC FAZY SZKOLENIOWEJ")
        self.textEdit_info_akus.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_akus.setFont(font_small)
        self.textEdit_info_akus.repaint()
        QtTest.QTest.qWait(2000)
        self.textEdit_info_akus.setTextBackgroundColor(white)
        self.textEdit_info_akus.setText("CZAS NA TEST")
        self.textEdit_info_akus.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_akus.setFont(font)
        self.textEdit_info_akus.repaint()
        QtTest.QTest.qWait(2000)
        for i in range(self.test_akus):
            self.textEdit_info_akus.setText("TEST")
            self.textEdit_info_akus.setAlignment(QtCore.Qt.AlignCenter)
            self.textEdit_info_akus.setFont(font)
            self.textEdit_info_akus.repaint()
            delay = random.randrange(2000, 4000)
            QtTest.QTest.qWait(delay)
            self.time_start_akus()
            QSound.play("laser-01.wav")
            self.textEdit_akus.repaint()
            QtTest.QTest.qWait(2000)
        self.textEdit_info_akus.setText("KONIEC TESTU")
        self.textEdit_info_akus.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_akus.setFont(font)
        self.textEdit_info_akus.repaint()
        QtTest.QTest.qWait(2000)
        self.textEdit_info_akus.setText("ZOBACZ WYNIKI")
        self.textEdit_info_akus.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_info_akus.setFont(font)
        self.textEdit_info_akus.repaint()
        QtTest.QTest.qWait(2000)

    def time_start_opt(self):
        self.start_opt = int(round(time.time() * 1000))
        print(self.start_opt)

    def time_start_akus(self):
        self.start_akus = int(round(time.time() * 1000))
        print(self.start_akus)

    def time_stop_opt(self):
        self.stop_opt = int(round(time.time() * 1000)) # pobranie czasu sys. w momencie zatrzymania
        self.reaction_time_opt(self.i)
        self.i += 1
        if self.i == self.test_opt + 1:
            self.i = 1
            QtTest.QTest.qWait(2000)
            self.textEdit_opt.setText("")
            self.textEdit_opt.repaint()

    def time_stop_akus(self):
        self.stop_akus = int(round(time.time() * 1000))
        print(self.stop_akus)
        self.reaction_time_akus(self.j)
        self.j += 1
        if self.j == self.test_akus + 1:
            self.j = 1
            QtTest.QTest.qWait(2000)
            self.textEdit_akus.setText("")
            self.textEdit_akus.repaint()

    def reaction_time_opt(self, i):
        self.textEdit_opt.append("{}. próba: ".format(i) + str(self.stop_opt - self.start_opt) + " ms")
        self.textEdit_opt.repaint()
        if self.i_test >= self.test_opt + 1:
            self.czas = self.stop_opt - self.start_opt
            self.opt_wyniki.append(str(self.czas))
            print(self.opt_wyniki)
            self.czas_opt += self.czas
            with open("results_opt.txt", "a") as file:
                file.write(str(self.czas))
                file.write("\n")
        self.i_test += 1

    def reaction_time_akus(self, j):
        self.textEdit_akus.append("{}. próba: ".format(j) + str(self.stop_akus - self.start_akus) + " ms")
        self.textEdit_akus.repaint()
        if self.j_test >= self.test_akus + 1:
            self.czas = self.stop_akus - self.start_akus
            self.akus_wyniki.append(str(self.czas))
            print(self.akus_wyniki)
            self.czas_akus += self.czas
            with open("results_akus.txt", "a") as file:
                file.write(str(self.czas))
                file.write("\n")
        self.j_test += 1

    def wyniki_opt(self):
        wynik = " ms, ".join(self.opt_wyniki)
        self.textEdit_opt.setText("Uzyskane czasy: " + wynik + " ms")
        self.textEdit_opt.repaint()
        sredni_czas = self.czas_opt/self.test_opt
        self.textEdit_opt.append("Twój średni czas: " + str(sredni_czas) + " ms")
        self.textEdit_opt.repaint()
        results = []
        with open("results_opt.txt", "r") as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                results.append(int(lines[i]))
        total_time = 0
        for num in results:
            total_time += num
        total_avrage_time = total_time/len(lines)
        self.textEdit_opt.append("Średni czas: " + str(total_avrage_time) + " ms")
        self.textEdit_opt.repaint()
        x = []
        for i in range(self.test_opt):
            x.append(i+1)
        plt.figure(num='Wyniki')
        plt.plot(x, self.opt_wyniki)
        plt.xticks(x)
        plt.ylabel("Czas [ms]")
        plt.xlabel("Numer próby")
        plt.show()

    def wyniki_akus(self):
        wynik = " ms, ".join(self.akus_wyniki)
        self.textEdit_akus.setText("Uzyskane czasy: " + wynik + " ms")
        self.textEdit_akus.repaint()
        sredni_czas = self.czas_akus/self.test_akus
        self.textEdit_akus.append("Twój średni czas: " + str(sredni_czas) + " ms")
        self.textEdit_akus.repaint()
        results = []
        with open("results_akus.txt", "r") as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                results.append(int(lines[i]))
        total_time = 0
        for num in results:
            total_time += num
        total_average_time = total_time/len(lines)
        self.textEdit_akus.append("Średni czas: " + str(total_average_time) + " ms")
        self.textEdit_akus.repaint()
        x = []
        for i in range(self.test_akus):
            x.append(i+1)

        plt.figure(num='Wyniki')
        plt.plot(x, self.akus_wyniki)
        plt.xticks(x)
        plt.ylabel("Czas [ms]")
        plt.xlabel("Numer próby")
        plt.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())