import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie, QGuiApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtTest, QtGui, QtCore, sip
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QLabel
import random
import time

MAX_TIMER = 30

class App(QWidget):
    EXIT_CODE_REBOOT = -123
    font = QtGui.QFont()
    font.setPointSize(30)
    red = QtGui.QColor(255, 0, 0)
    orange = QtGui.QColor(249, 118, 2)
    green = QtGui.QColor(0, 255, 0)

    def __init__(self):
        super().__init__()
        # self.setGeometry(100, 100, 1000, 900)
        self.setFixedSize(1000, 900)
        self.move(500, 0)
        self.setWindowTitle('Linia produkcyjna')
        self.setStyleSheet("background-color: white")
        self.initUI()

    def initUI(self):
        self.labelLogin = QLabel(self)
        self.labelLogin.setFixedSize(50, 20)
        self.labelLogin.move(450, 350)
        self.labelLogin.setText("Login:")

        self.labelPassword = QLabel(self)
        self.labelPassword.setFixedSize(70, 20)
        self.labelPassword.move(450, 410)
        self.labelPassword.setText("Password:")

        self.lineEditLogin = QLineEdit(self)
        self.lineEditLogin.setGeometry(450, 370, 150, 30)

        self.lineEditPassword = QLineEdit(self)
        self.lineEditPassword.setGeometry(450, 430, 150, 30)
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton(self)
        self.button_login.setText("LOG IN")
        self.button_login.move(450, 470)
        self.button_login.setStyleSheet("background-color: #d4d3d5")
        self.button_login.clicked.connect(self.login)

        # self.form = QFormLayout()
        # self.form.addRow(QLabel("Login: "), self.lineEditLogin)
        # self.form.addRow(QLabel("Hasło: "), self.lineEditPassword)
        # self.form.addWidget(self.button_login)
        #
        # self.setLayout(self.form)

        self.show()

    def initUI2(self):
        self.alarm = 0
        self.start_bool = False
        self.breakdown = False

        self.labelProductionLine = QLabel(self)
        self.labelProductionLine.setFixedSize(200, 20)
        self.labelProductionLine.move(50, 400)
        self.labelProductionLine.setText("Prędkość linii produkcyjnej:")

        self.labelFan = QLabel(self)
        self.labelFan.setFixedSize(200, 20)
        self.labelFan.move(550, 400)
        self.labelFan.setText("Prędkość wiatraka:")

        self.labelProdLineUsage = QLabel(self)
        self.labelProdLineUsage.setFixedSize(200, 20)
        self.labelProdLineUsage.move(50, 480)
        self.labelProdLineUsage.setText("Wydajność linii produkcyjnej:")

        self.labelFanUsage = QLabel(self)
        self.labelFanUsage.setFixedSize(200, 20)
        self.labelFanUsage.move(550, 480)
        self.labelFanUsage.setText("Użycie wiatraka:")

        self.textEditProdLineUsage = QTextEdit(self)
        self.textEditProdLineUsage.setFixedSize(100, 20)
        self.textEditProdLineUsage.move(230, 480)
        self.textEditProdLineUsage.setReadOnly(True)

        self.textEditFanUsage = QTextEdit(self)
        self.textEditFanUsage.setFixedSize(100, 20)
        self.textEditFanUsage.move(660, 480)
        self.textEditFanUsage.setReadOnly(True)

        self.textEditInfo = QTextEdit(self)
        self.textEditInfo.setFixedSize(485, 200)
        self.textEditInfo.move(300, 550)

        self.button_start = QPushButton(self)
        self.button_start.setText("START")
        self.button_start.setFixedSize(150, 100)
        self.button_start.move(450, 770)
        self.button_start.setStyleSheet("background-color: yellow")
        self.button_start.clicked.connect(self.start)

        self.button_stop = QPushButton(self)
        self.button_stop.setText("STOP")
        self.button_stop.setFixedSize(150, 100)
        self.button_stop.move(600, 770)
        self.button_stop.setStyleSheet("background-color: red")
        self.button_stop.clicked.connect(self.stop)

        self.button_instruction = QPushButton(self)
        self.button_instruction.setText("INSTRUKCJA")
        self.button_instruction.setFixedSize(150, 100)
        self.button_instruction.move(300, 770)
        self.button_instruction.setStyleSheet("background-color: #d4d3d5")
        self.button_instruction.clicked.connect(self.instruction)

        self.button_1 = QPushButton(self)
        self.button_1.setText("1")
        self.button_1.setFixedSize(150, 150)
        self.button_1.move(300, 770)
        self.button_1.setFont(self.font)
        self.button_1.setStyleSheet("background-color: #00e9ff")
        self.button_1.clicked.connect(self.button_1clicked)

        self.button_2 = QPushButton(self)
        self.button_2.setText("2")
        self.button_2.setFixedSize(150, 150)
        self.button_2.move(300, 770)
        self.button_2.setFont(self.font)
        self.button_2.setStyleSheet("background-color: #ff00cb")
        self.button_2.clicked.connect(self.button_2clicked)

        self.button_3 = QPushButton(self)
        self.button_3.setText("3")
        self.button_3.setFixedSize(150, 150)
        self.button_3.setFont(self.font)
        self.button_3.setStyleSheet("background-color: #00ff21")
        self.button_3.clicked.connect(self.button_3clicked)

        self.labelButtonClickInfo = QLabel(self)
        self.labelButtonClickInfo.setFixedSize(450, 60)
        self.labelButtonClickInfo.setStyleSheet("background-color: white; font-size: 22pt; qproperty-alignment: AlignCenter")
        #self.labelButtonClickInfo.setText("Naciśnij przycisk!")

        self.gif_prod = QLabel(self)
        self.movie_prod = QMovie("prod3d.gif")
        self.gif_prod.setMovie(self.movie_prod)
        self.gif_prod.setGeometry(250, 20, 400, 329)
        self.movie_prod.setSpeed(0)
        self.movie_prod.start()

        self.gif_fan = QLabel(self)
        self.movie_fan = QMovie("fan3.gif")
        self.gif_fan.setMovie(self.movie_fan)
        self.gif_fan.setGeometry(700, 80, 269, 269)
        self.movie_fan.setSpeed(0)
        self.movie_fan.start()

        self.slider_prod = QSlider(Qt.Horizontal)
        self.slider_prod.setMinimum(40)
        self.slider_prod.setMaximum(200)
        self.slider_prod.setValue(100)
        self.slider_prod.setTickInterval(10)
        self.slider_prod.setTickPosition(QSlider.TicksBelow)
        self.slider_prod.setEnabled(False)
        self.slider_prod.valueChanged[int].connect(self.prod_value)

        self.slider_fan = QSlider(Qt.Horizontal)
        self.slider_fan.setGeometry(200, 333, 312, 321)
        self.slider_fan.setMinimum(40)
        self.slider_fan.setMaximum(200)
        self.slider_fan.setValue(100)
        self.slider_fan.setTickInterval(10)
        self.slider_fan.setTickPosition(QSlider.TicksBelow)
        self.slider_fan.setEnabled(False)
        self.slider_fan.valueChanged[int].connect(self.fan_value)

        grid = QGridLayout()
        grid.addWidget(self.gif_fan, 1, 3, Qt.AlignCenter)
        grid.addWidget(self.gif_prod, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.labelProdLineUsage, 4, 1)
        grid.addWidget(self.labelFanUsage, 4, 3)
        grid.addWidget(self.slider_prod, 3, 1)
        grid.addWidget(self.slider_fan, 3, 3)
        grid.addWidget(self.labelProductionLine, 2, 1)
        grid.addWidget(self.labelFan, 2, 3)
        grid.addWidget(self.textEditProdLineUsage, 4, 1, Qt.AlignCenter)
        grid.addWidget(self.textEditFanUsage, 4, 3, Qt.AlignCenter)
        grid.addWidget(self.textEditInfo, 5, 1, Qt.AlignCenter)
        grid.addWidget(self.button_instruction, 6, 1)
        grid.addWidget(self.button_start, 6, 1, Qt.AlignCenter)
        grid.addWidget(self.button_stop, 6, 1, Qt.AlignRight)
        grid.addWidget(self.button_1, 5, 3)
        grid.addWidget(self.button_2, 5, 3, Qt.AlignCenter)
        grid.addWidget(self.button_3, 5, 3, Qt.AlignRight)
        grid.addWidget(self.labelButtonClickInfo, 6, 3, Qt.AlignCenter | Qt.AlignTop)

        self.setLayout(grid)

        self.show()

    def button_1clicked(self):
        self.button_clicked(1)

    def button_2clicked(self):
        self.button_clicked(2)

    def button_3clicked(self):
        self.button_clicked(3)

    def button_clicked(self, num):
        if num == self.buttonToClick:
            self.timerStart = time.time()
            self.button_color = self.button_color_function()

    def button_color_function(self):
        color = random.randint(1, 3)
        if color == 1:
            self.buttonToClick = 1
            return "Niebieski"
        if color == 2:
            self.buttonToClick = 2
            return "Rożowy"
        if color == 3:
            self.buttonToClick = 3
            return "Zielony"

    def start(self):
        if not self.start_bool:
            self.failure_iter_timer = 0
            self.start_bool = True
            self.movie_prod.setSpeed(100)
            self.movie_fan.setSpeed(100)
            self.slider_fan.setEnabled(True)
            self.slider_prod.setEnabled(True)
            self.textEditFanUsage.setText("50")
            self.textEditProdLineUsage.setText("50")

            self.timerStart = time.time()
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.timerForLogout)
            self.timer.start(100)

            self.button_color = self.button_color_function()

    def stop(self):
        if self.start_bool:
            self.movie_prod.setSpeed(0)
            self.movie_fan.setSpeed(0)
            self.slider_fan.setEnabled(False)
            self.slider_prod.setEnabled(False)

            self.start_bool = False
            self.timer.stop()

    def instruction(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Instrukcja obsługi linii produkcyjnej")
        msg.setInformativeText("Linia zaczyna działać po naciśnięciu przycisku start. Można regulować prędkość jej działania za pomocą suwaków, a w przypadku awarii można niezależnie zmienić prędkość wiatraku. ")
        msg.exec_()

    def failure_function(self, failure):
        if 5 <= failure <= 10:
            self.breakdown = True
        if 5 <= failure <= 7:
            self.textEditInfo.setTextBackgroundColor(self.red)
            self.textEditInfo.setText("AWARIA")
            self.textEditInfo.setFont(self.font)
            self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
            self.textEditInfo.repaint()
            self.movie_prod.setSpeed(0)
            self.slider_prod.setEnabled(False)
            self.slider_fan.setEnabled(False)
            for i in range(100):
                QGuiApplication.processEvents()
                self.timerForLogout()
                QtTest.QTest.qWait(30)
            #QtTest.QTest.qWait(3000)
            self.textEditInfo.setTextBackgroundColor(self.orange)
            self.textEditInfo.setText("OCHŁADZANIE LINII PRODUKCYJNEJ")
            self.textEditInfo.setFont(self.font)
            self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
            self.textEditInfo.repaint()
            self.slider_fan.setValue(200)
            for i in range(100):
                QGuiApplication.processEvents()
                self.timerForLogout()
                QtTest.QTest.qWait(30)
            #QtTest.QTest.qWait(3000)
            self.slider_prod.setEnabled(True)
            self.slider_fan.setEnabled(True)
            self.textEditInfo.setTextBackgroundColor(self.green)
            self.textEditInfo.setText("LINIA PRODUKCYJNA OCHŁODZONA, DZIAŁANIE WZNOWIONE")
            self.textEditInfo.setFont(self.font)
            self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
            self.movie_prod.setSpeed(self.slider_fan.value())
            self.slider_prod.setValue(100)
            self.textEditInfo.repaint()
        elif 8 <= failure <= 10:
            self.textEditInfo.setTextBackgroundColor(self.red)
            self.textEditInfo.setText("BŁĄD KRYTYCZNY, DZIAŁAJ")
            self.textEditInfo.setFont(self.font)
            self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
            self.textEditInfo.repaint()
            self.movie_prod.setSpeed(0)
            self.slider_prod.setEnabled(False)
            self.slider_fan.setEnabled(True)
            for i in range(100):
                QGuiApplication.processEvents()
                self.timerForLogout()
                if self.slider_fan.value() > 180:
                    break
                QtTest.QTest.qWait(100)
            if self.slider_fan.value() > 180:
                self.slider_prod.setEnabled(True)
                self.slider_fan.setEnabled(True)
                self.textEditInfo.setTextBackgroundColor(self.green)
                self.textEditInfo.setText("LINIA PRODUKCYJNA OCHŁODZONA, DZIAŁANIE WZNOWIONE")
                self.textEditInfo.setFont(self.font)
                self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
                self.movie_prod.setSpeed(self.slider_fan.value())
                self.textEditInfo.repaint()
                self.slider_prod.setValue(100)
                QtTest.QTest.qWait(3000)
            else:
                self.textEditInfo.setTextBackgroundColor(self.red)
                self.textEditInfo.setText("BRAK PODJĘTEGO DZIAŁANIA, NASTĄPI WYLOGOWANIE")
                self.textEditInfo.setFont(self.font)
                self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
                self.textEditInfo.repaint()
                QtTest.QTest.qWait(3000)
                qApp.exit(App.EXIT_CODE_REBOOT)
        self.breakdown = False
        print("KONIEC AWARII")

    def timerForLogout(self):
        self.alarm = MAX_TIMER - (float(time.time()) - float(self.timerStart))
        if not self.breakdown:
            self.failure_iter_timer += 1
        self.labelButtonClickInfo.setText("Naciśnij " + "<font color=\"black\"><b>" +
                                          self.button_color + "<b></font>" + " przycisk!<br>" + str(self.alarm)[:4])

        if self.alarm < 5:
            sound = "beep-01a.wav"
            QSound.play(sound)

        # Co 10 sekund losuje liczbę określającą czy nastąpi awaria
        if self.failure_iter_timer % 100 == 0 and not self.breakdown:
            print(self.failure_iter_timer)
            if self.slider_prod.value() < 180:
                failure = random.randint(0, 10)
                print("sprawdzanie bledow: " + str(failure))
                self.failure_function(failure)

        if self.alarm < 0:
            print("alarm")
            qApp.exit(App.EXIT_CODE_REBOOT)

        return

    def login(self):
        input_login = self.lineEditLogin.text()
        input_password = self.lineEditPassword.text()

        if (input_login == "monika" or input_login == "krzys") and input_password == "ask":
            #print("Monika jest super")
            self.button_login.deleteLater()
            self.lineEditLogin.deleteLater()
            self.lineEditPassword.deleteLater()
            self.labelLogin.deleteLater()
            self.labelPassword.deleteLater()
            self.initUI2()

    def prod_value(self):
        self.prod_value = self.slider_prod.value()
        self.movie_prod.setSpeed(self.prod_value)
        self.slider_fan.setValue(self.prod_value)
        self.textEditProdLineUsage.setText(str(self.prod_value/2))
        self.textEditFanUsage.setText(str(self.prod_value/2))
        if self.prod_value > 180:
            self.textEditInfo.setTextBackgroundColor(self.red)
            self.textEditInfo.setText("Zbyt duża prędkość działania, nastąpi zwalnianie!")
            self.textEditInfo.setFont(self.font)
            self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
            self.textEditInfo.repaint()
            self.slider_prod.setEnabled(False)
            self.slider_fan.setEnabled(False)
            QtTest.QTest.qWait(2000)
            self.prod_value = self.prod_value - 20
            for i in range(8):
                self.textEditInfo.setTextBackgroundColor(self.orange)
                self.textEditInfo.setText("Zwalnianie!")
                self.textEditInfo.setFont(self.font)
                self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
                self.textEditInfo.repaint()
                self.prod_value = self.prod_value - 10
                self.slider_prod.setValue(self.prod_value)
                QtTest.QTest.qWait(500)
            self.slider_prod.setEnabled(True)
            self.slider_fan.setEnabled(True)
            self.textEditInfo.setTextBackgroundColor(self.green)
            self.textEditInfo.setText("Linia produkcyjna ochłodzona!")
            self.textEditInfo.setFont(self.font)
            self.textEditInfo.setAlignment(QtCore.Qt.AlignCenter)
            self.textEditInfo.repaint()

    def fan_value(self):
        fan_value = self.slider_fan.value()
        self.movie_fan.setSpeed(fan_value)
        self.textEditFanUsage.setText(str(fan_value/2))


if __name__ == '__main__':
    currentExitCode = App.EXIT_CODE_REBOOT
    while currentExitCode == App.EXIT_CODE_REBOOT:
        a = QApplication(sys.argv)
        w = App()
        w.show()
        currentExitCode = a.exec_()
        a = None  # delete the QApplication object