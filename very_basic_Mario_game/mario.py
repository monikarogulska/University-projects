from xml.dom.minidom import Document

from PyQt5 import QtGui, QtCore, QtTest
import sys
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from xml.dom import minidom
import json


class Window(QMainWindow):
    i = 0
    posy = 0
    top = False
    money = 0
    money1 = 0
    money2 = 0
    money3 = 0
    money4 = 0
    mushroom_alive = 1
    step = 0
    character = 1
    moves = {}

    doc = Document()
    root = doc.createElement("game")
    js = open("data.txt", 'w')

    def __init__(self):
        super().__init__()

        self.title = "Mario"
        self.top = 600
        self.left = 100
        self.width = 1000
        self.height = 800

        self.InitWindow()

    def InitWindow(self):
        self.scene = QGraphicsScene()

        self.brownPen = QPen(QColor(109, 51, 24))
        self.brownPen.setWidth(3)

        self.redPen = QPen(Qt.red)
        self.redPen.setWidth(3)

        self.yellowBrush = QBrush(Qt.yellow)
        self.brownBrush = QBrush(QColor(109, 51, 24))

        self.mario_bgr = QtGui.QPixmap("background.jpg")
        self.mario_bgr = self.mario_bgr.scaled(995, 795)
        self.bgr = self.scene.addPixmap(self.mario_bgr)

        self.rect_size_x = 30
        self.rect_size_y = 40

        self.rect1_x = 333
        self.rect1_y = 510
        self.rect1 = self.scene.addRect(self.rect1_x, self.rect1_y, self.rect_size_x, self.rect_size_y, self.brownPen,
                                        self.yellowBrush)
        self.rectangle1 = True
        self.rect2_x = 167
        self.rect2 = self.scene.addRect(self.rect2_x, self.rect1_y, self.rect_size_x, self.rect_size_y, self.brownPen,
                                        self.yellowBrush)
        self.rectangle2 = True
        self.rect3_x = 400
        self.rect3 = self.scene.addRect(self.rect3_x, self.rect1_y, self.rect_size_x, self.rect_size_y, self.brownPen,
                                        self.yellowBrush)
        self.rectangle3 = True
        self.rect4_x = 366
        self.rect4_y = 341
        self.rect4 = self.scene.addRect(self.rect4_x, self.rect4_y, self.rect_size_x, self.rect_size_y, self.brownPen,
                                        self.yellowBrush)
        self.rectangle4 = True

        if self.character == 1:
            self.mario_pic = QtGui.QPixmap("mario.png")
            self.mario_pic = self.mario_pic.scaled(55, 80)
            self.mario = self.scene.addPixmap(self.mario_pic)
            self.x = 15
            self.y = 600
            self.moves["x"] = self.x
            self.moves["y"] = self.y
            self.moves['money'] = 0
            json.dump(self.moves, self.js)
            self.js.seek(0)
            self.mario_pos = self.mario.mapFromScene(self.x, self.y)
            self.mario.setPos(self.mario_pos)
        elif self.character == 2:
            self.luigi_pic = QtGui.QPixmap("luigi.png")
            self.luigi_pic = self.luigi_pic.scaled(55, 80)
            self.luigi = self.scene.addPixmap(self.luigi_pic)
            self.x_luigi = 650
            self.y_luigi = 600
            self.moves["x"] = self.x
            self.moves["y"] = self.y
            self.moves['money'] = 0
            self.luigi_pos = self.luigi.mapFromScene(self.x_luigi, self.y_luigi)
            self.luigi.setPos(self.luigi_pos)
        # self.mario.setFlag(QGraphicsItem.ItemIsFocusable, True)
        # self.scene.setFocus(self.mario)

        self.mushroom_pic = QtGui.QPixmap("mushroom.png")
        self.mushroom_pic = self.mushroom_pic.scaled(50, 50)
        self.mushroom = self.scene.addPixmap(self.mushroom_pic)
        self.x_mushroom = 650
        self.y_mushroom = 630
        self.mushroom_pos = self.mushroom.mapFromScene(self.x_mushroom, self.y_mushroom)
        self.mushroom.setPos(self.mushroom_pos)
        self.mushroom.setFlag(QGraphicsItem.ItemIsFocusable, True)

        view = QGraphicsView(self.scene, self)
        view.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.button_start = QPushButton('', self)
        self.button_start.setIcon(QtGui.QIcon("start.png"))
        self.button_start.setIconSize(QtCore.QSize(180, 70))
        self.button_start.setStyleSheet("background-color: white")
        self.button_start.resize(200, 50)
        self.button_start.move(400, 20)
        self.button_start.clicked.connect(self.move_mushroom)

        # self.button_save = QPushButton('Zapisz', self)
        # self.button_save.setStyleSheet("background-color: white")
        # self.button_save.resize(100, 50)
        # self.button_save.move(700, 20)
        # self.button_save.clicked.connect(self.save)
        #
        # self.button_read = QPushButton('Odczytaj', self)
        # self.button_read.setStyleSheet("background-color: white")
        # self.button_read.resize(100, 50)
        # self.button_read.move(800, 20)
        # self.button_read.clicked.connect(self.read)
        #
        # self.button_save_history = QPushButton('Zapisz \ndo historii', self)
        # self.button_save_history.setStyleSheet("background-color: white")
        # self.button_save_history.resize(100, 50)
        # self.button_save_history.move(700, 70)
        # self.button_save_history.clicked.connect(self.save_history)
        #
        # self.button_stop = QPushButton('stop', self)
        # self.button_stop.resize(200, 50)
        # self.button_stop.move(400, 100)
        # self.button_stop.clicked.connect(self.stop)

        self.labelMoney = QLabel(self)
        self.labelMoney.setFixedSize(780, 30)
        self.labelMoney.move(10, 20)
        self.labelMoney.setText("Monety: {}".format(self.money))
        self.labelMoney.setStyleSheet('font-size: 30pt; font-family: Courier;')

        # self.labelSteps = QLabel(self)
        # self.labelSteps.setFixedSize(780, 30)
        # self.labelSteps.move(700, 130)
        # self.labelSteps.setText("Zapisane kroki: {}".format(self.step))
        # self.labelSteps.setStyleSheet('font-size: 16pt; font-family: Courier;')

        # self.TextEditStep = QTextEdit(self)
        # self.TextEditStep.setFixedSize(30, 30)
        # self.TextEditStep.move(700, 170)
        # self.TextEditStep.setAlignment(Qt.AlignCenter)

        # self.button_read_history = QPushButton('Odczytaj z historii', self)
        # self.button_read_history.setStyleSheet("background-color: white")
        # self.button_read_history.resize(150, 30)
        # self.button_read_history.move(740, 170)
        # self.button_read_history.clicked.connect(self.read_history)

        self.show()

    def stop(self):
        QtTest.QTest.qWait(10000)

    def save(self):

        self.doc = Document()
        root = self.doc.createElement("game")
        self.doc.appendChild(root)
        mario = self.doc.createElement("mario_coords")
        mushroom = self.doc.createElement("mushroom_coords")
        money = self.doc.createElement("money")
        rectangles = self.doc.createElement("rectangles")
        money_iftaken = self.doc.createElement("taken")
        mushroom_dead = self.doc.createElement("mushroom_alive")
        root.appendChild(mario)
        root.appendChild(mushroom)
        root.appendChild(money)
        root.appendChild(rectangles)
        root.appendChild(money_iftaken)
        root.appendChild(mushroom_dead)
        mario.setAttribute("x", str(self.x))
        mario.setAttribute("y", str(self.y))
        mushroom.setAttribute("x", str(self.x_mushroom))
        mushroom.setAttribute("y", str(self.y_mushroom))
        money.setAttribute("amount", str(self.money))
        money_iftaken.setAttribute("rec1", str(self.money1))
        money_iftaken.setAttribute("rec2", str(self.money2))
        money_iftaken.setAttribute("rec3", str(self.money3))
        money_iftaken.setAttribute("rec4", str(self.money4))
        rectangles.setAttribute("rec1", str(self.rectangle1))
        rectangles.setAttribute("rec2", str(self.rectangle2))
        rectangles.setAttribute("rec3", str(self.rectangle3))
        rectangles.setAttribute("rec4", str(self.rectangle4))
        mushroom_dead.setAttribute("alive", str(self.mushroom_alive))
        self.doc.writexml(open('status.xml', 'w'),
                          indent="  ",
                          addindent="  ",
                          newl='\n')

    def read(self):

        mydoc = minidom.parse("status.xml")
        mario = mydoc.getElementsByTagName("mario_coords")
        self.x = int(mario[0].attributes["x"].value)
        self.y = int(mario[0].attributes["y"].value)
        self.mario.setPos(self.x, self.y)
        mushroom = mydoc.getElementsByTagName("mushroom_coords")
        self.mushroom_x = mushroom[0].attributes["x"].value
        self.mushroom_y = mushroom[0].attributes["y"].value
        self.mushroom.setPos(int(self.mushroom_x), int(self.mushroom_y))
        money = mydoc.getElementsByTagName("money")
        self.money = int(money[0].attributes["amount"].value)
        self.labelMoney.setText("Monety: {}".format(self.money))
        money_if_taken = mydoc.getElementsByTagName("taken")
        self.money1 = int(money_if_taken[0].attributes["rec1"].value)
        self.money2 = int(money_if_taken[0].attributes["rec2"].value)
        self.money3 = int(money_if_taken[0].attributes["rec3"].value)
        self.money4 = int(money_if_taken[0].attributes["rec4"].value)
        mushroom_lives = mydoc.getElementsByTagName("mushroom_alive")
        self.mushroom_alive = int(mushroom_lives[0].attributes["alive"].value)
        print("mushroom", self.mushroom_alive)
        if self.mushroom_alive == 1:
            self.mushroom = self.scene.addPixmap(self.mushroom_pic)
            self.mushroom.setPos(self.x_mushroom, self.y_mushroom)
        rectangles = mydoc.getElementsByTagName("rectangles")
        self.rectangle1 = rectangles[0].attributes["rec1"].value
        self.rectangle2 = rectangles[0].attributes["rec2"].value
        self.rectangle3 = rectangles[0].attributes["rec3"].value
        self.rectangle4 = rectangles[0].attributes["rec4"].value
        for enum, rectangle in enumerate([self.rectangle1, self.rectangle2, self.rectangle3, self.rectangle4]):
            print(rectangle)
            print(enum)
            if rectangle == "True":
                if enum == 0:
                    self.rect1 = self.scene.addRect(self.rect1_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
                if enum == 1:
                    self.rect2 = self.scene.addRect(self.rect2_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
                if enum == 2:
                    self.rect3 = self.scene.addRect(self.rect3_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
                if enum == 3:
                    self.rect4 = self.scene.addRect(self.rect4_x, self.rect4_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
            else:
                if enum == 0:
                    self.rect1 = self.scene.addRect(self.rect1_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
                if enum == 1:
                    self.rect2 = self.scene.addRect(self.rect2_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
                if enum == 2:
                    self.rect3 = self.scene.addRect(self.rect3_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
                if enum == 3:
                    self.rect4 = self.scene.addRect(self.rect4_x, self.rect4_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
        QtTest.QTest.qWait(500)

    def save_history(self):

        self.step += 1
        self.labelSteps.setText("Zapisane kroki: {}".format(self.step))
        self.doc.appendChild(self.root)
        self.save_no = self.doc.createElement("save%i"%self.step)
        self.root.appendChild(self.save_no)
        mario = self.doc.createElement("mario_coords%i" % self.step)
        mushroom = self.doc.createElement("mushroom_coords%i" % self.step)
        money = self.doc.createElement("money%i" % self.step)
        rectangles = self.doc.createElement("rectangles%i" % self.step)
        money_iftaken = self.doc.createElement("taken%i" % self.step)
        mushroom_dead = self.doc.createElement("mushroom_alive%i" % self.step)
        self.save_no.appendChild(mario)
        self.save_no.appendChild(mushroom)
        self.save_no.appendChild(money)
        self.save_no.appendChild(rectangles)
        self.save_no.appendChild(money_iftaken)
        self.save_no.appendChild(mushroom_dead)
        self.root.appendChild(mario)
        self.root.appendChild(mushroom)
        self.root.appendChild(money)
        self.root.appendChild(rectangles)
        self.root.appendChild(money_iftaken)
        self.root.appendChild(mushroom_dead)
        mario.setAttribute("x", str(self.x))
        mario.setAttribute("y", str(self.y))
        mushroom.setAttribute("x", str(self.x_mushroom))
        mushroom.setAttribute("y", str(self.y_mushroom))
        money.setAttribute("amount", str(self.money))
        money_iftaken.setAttribute("rec1", str(self.money1))
        money_iftaken.setAttribute("rec2", str(self.money2))
        money_iftaken.setAttribute("rec3", str(self.money3))
        money_iftaken.setAttribute("rec4", str(self.money4))
        rectangles.setAttribute("rec1", str(self.rectangle1))
        rectangles.setAttribute("rec2", str(self.rectangle2))
        rectangles.setAttribute("rec3", str(self.rectangle3))
        rectangles.setAttribute("rec4", str(self.rectangle4))
        mushroom_dead.setAttribute("alive", str(self.mushroom_alive))
        self.doc.writexml(open('history.xml', 'w'),
                          indent="  ",
                          addindent="  ",
                          newl='\n')

    def read_history(self):

        input = int(self.TextEditStep.toPlainText())
        print(input)

        mydoc = minidom.parse("history.xml")
        mario = mydoc.getElementsByTagName("mario_coords%i" % input)
        print(mario)
        self.x = int(mario[0].attributes["x"].value)
        self.y = int(mario[0].attributes["y"].value)
        self.mario.setPos(self.x, self.y)
        mushroom = mydoc.getElementsByTagName("mushroom_coords%i" % input)
        self.mushroom_x = mushroom[0].attributes["x"].value
        self.mushroom_y = mushroom[0].attributes["y"].value
        self.mushroom.setPos(int(self.mushroom_x), int(self.mushroom_y))
        money = mydoc.getElementsByTagName("money%i" % input)
        self.money = int(money[0].attributes["amount"].value)
        self.labelMoney.setText("Monety: {}".format(self.money))
        money_if_taken = mydoc.getElementsByTagName("taken%i" % input)
        self.money1 = int(money_if_taken[0].attributes["rec1"].value)
        self.money2 = int(money_if_taken[0].attributes["rec2"].value)
        self.money3 = int(money_if_taken[0].attributes["rec3"].value)
        self.money4 = int(money_if_taken[0].attributes["rec4"].value)
        mushroom_lives = mydoc.getElementsByTagName("mushroom_alive%i" % input)
        self.mushroom_alive = int(mushroom_lives[0].attributes["alive"].value)
        print("mushroom", self.mushroom_alive)
        if self.mushroom_alive == 1:
            self.mushroom = self.scene.addPixmap(self.mushroom_pic)
            self.mushroom.setPos(self.x_mushroom, self.y_mushroom)
        elif self.mushroom_alive == 0:
            self.scene.removeItem(self.mushroom)
        rectangles = mydoc.getElementsByTagName("rectangles%i" % input)
        self.rectangle1 = rectangles[0].attributes["rec1"].value
        self.rectangle2 = rectangles[0].attributes["rec2"].value
        self.rectangle3 = rectangles[0].attributes["rec3"].value
        self.rectangle4 = rectangles[0].attributes["rec4"].value
        for enum, rectangle in enumerate([self.rectangle1, self.rectangle2, self.rectangle3, self.rectangle4]):
            print(rectangle)
            print(enum)
            if rectangle == "True":
                if enum == 0:
                    self.rect1 = self.scene.addRect(self.rect1_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
                if enum == 1:
                    self.rect2 = self.scene.addRect(self.rect2_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
                if enum == 2:
                    self.rect3 = self.scene.addRect(self.rect3_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
                if enum == 3:
                    self.rect4 = self.scene.addRect(self.rect4_x, self.rect4_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.yellowBrush)
            else:
                if enum == 0:
                    self.rect1 = self.scene.addRect(self.rect1_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
                if enum == 1:
                    self.rect2 = self.scene.addRect(self.rect2_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
                if enum == 2:
                    self.rect3 = self.scene.addRect(self.rect3_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
                if enum == 3:
                    self.rect4 = self.scene.addRect(self.rect4_x, self.rect4_y, self.rect_size_x, self.rect_size_y,
                                                    self.brownPen, self.brownBrush)
        QtTest.QTest.qWait(500)

    def jump(self):
        for i in range(25):
            self.y -= 10
            self.moves['y'] = self.y
            self.mario.setPos(self.x, self.y)
            self.posy += 1
            QtTest.QTest.qWait(50)
            if self.y == self.rect1_y + 40 and self.rect1_x - 30 <= self.x <= self.rect1_x + 10:
                self.rect1 = self.scene.addRect(self.rect1_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                self.brownPen, self.brownBrush)
                self.rectangle1 = False
                if self.money1 == 0:
                    self.money += 100
                    self.labelMoney.setText("Monety: {}".format(self.money))
                    self.money1 = 1
                    self.moves['money'] += 100
                break
            if self.y == self.rect1_y + 40 and self.rect2_x - 30 <= self.x <= self.rect2_x + 10:
                self.rect2 = self.scene.addRect(self.rect2_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                self.brownPen, self.brownBrush)
                self.rectangle2 = False
                if self.money2 == 0:
                    self.money += 100
                    self.labelMoney.setText("Monety: {}".format(self.money))
                    self.money2 = 1
                    self.moves['money'] += 100
                break
            if self.y == self.rect1_y + 40 and self.rect3_x - 30 <= self.x <= self.rect3_x + 10:
                self.rect3 = self.scene.addRect(self.rect3_x, self.rect1_y, self.rect_size_x, self.rect_size_y,
                                                self.brownPen, self.brownBrush)
                self.rectangle3 = False
                if self.money3 == 0:
                    self.money += 100
                    self.labelMoney.setText("Monety: {}".format(self.money))
                    self.money3 = 1
                    self.moves['money'] += 100
                break
            if self.y == self.rect4_y + 40 and self.rect4_x - 30 <= self.x <= self.rect4_x + 10:
                print("jestem")
                self.rect4 = self.scene.addRect(self.rect4_x, self.rect4_y, self.rect_size_x, self.rect_size_y,
                                                self.brownPen, self.brownBrush)
                self.rectangle4 = False
                if self.money4 == 0:
                    self.money += 100
                    self.labelMoney.setText("Monety: {}".format(self.money))
                    self.money4 = 1
                    self.moves['money'] += 100
                break
        for i in range(self.posy):
            self.posy = 0
            self.y += 10
            self.moves['y'] = self.y
            self.mario.setPos(self.x, self.y)
            QtTest.QTest.qWait(50)
            if self.y + 80 == self.y_mushroom and self.x_mushroom - 35 < self.x < self.x_mushroom + 35:
                self.scene.removeItem(self.mushroom)
            if self.y + 80 == self.rect1_y and self.rect2_x - 50 <= self.x <= self.rect2_x + 10:
                self.top = True
                break
            if self.y + 80 == self.rect1_y and self.rect1_x - 70 <= self.x <= self.rect3_x + 50:
                self.top = True
                break

    def jump_right(self):
        for i in range(15):
            self.x += 7
            self.y -= 15
            self.moves["x"] = self.x
            self.moves["y"] = self.y
            self.mario.setPos(self.x, self.y)
            QtTest.QTest.qWait(100)
        self.x += 17
        self.moves["x"] = self.x
        self.mario.setPos(self.x, self.y)
        QtTest.QTest.qWait(100)
        for i in range(15):
            self.x += 7
            self.y += 15
            self.moves["x"] = self.x
            self.moves["y"] = self.y
            self.mario.setPos(self.x, self.y)
            QtTest.QTest.qWait(100)
            if self.y_mushroom - 40 < self.y < self.y_mushroom and self.x_mushroom - 40 < self.x < self.x_mushroom + 40:
                self.scene.removeItem(self.mushroom)

    def jump_left(self):
        for i in range(15):
            self.x -= 7
            self.y -= 15
            self.moves["x"] = self.x
            self.moves["y"] = self.y
            self.mario.setPos(self.x, self.y)
            QtTest.QTest.qWait(100)
        self.x -= 17
        self.moves["x"] = self.x
        self.mario.setPos(self.x, self.y)
        QtTest.QTest.qWait(100)
        for i in range(15):
            self.x -= 7
            self.y += 15
            self.moves["x"] = self.x
            self.moves["y"] = self.y
            self.mario.setPos(self.x, self.y)
            QtTest.QTest.qWait(100)
            if self.y + 80 == self.y_mushroom and self.x_mushroom - 35 < self.x < self.x_mushroom + 35:
                self.scene.removeItem(self.mushroom)

    def fall(self):
        while self.y < 600:
            self.y += 10
            self.moves['y'] = self.y
            QtTest.QTest.qWait(50)
            self.mario.setPos(self.x, self.y)
        self.top = False

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_D:
            self.x = self.x + 10
            self.mario.setPos(self.x, self.y)
            self.moves["x"] = self.x
            json.dump(self.moves, self.js)
            self.js.seek(0)
            if self.top == True and self.y + 80 == self.rect1_y and self.x > self.rect2_x + 10:
                self.fall()
            if self.top == True and self.y + 80 == self.rect1_y and self.rect3_x + 60 > self.x:
                self.fall()
        elif event.key() == QtCore.Qt.Key_A:
            self.x = self.x - 10
            self.mario.setPos(self.x, self.y)
            self.moves["x"] = self.x
            json.dump(self.moves, self.js)
            self.js.seek(0)
            if self.top == True and self.y + 80 == self.rect1_y and self.x < self.rect2_x - 60:
                self.fall()
            if self.top == True and self.y + 80 == self.rect1_y and self.x < self.rect1_x - 60:
                self.fall()
        elif event.key() == QtCore.Qt.Key_W:
            self.jump()
        elif event.key() == QtCore.Qt.Key_E:
            self.jump_right()
        elif event.key() == QtCore.Qt.Key_Q:
            self.jump_left()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            shot = self.scene.addLine(self.x + 50, self.y + 50, event.x(), event.y(), self.redPen)
            QtTest.QTest.qWait(50)
            if self.mushroom_alive == 1:
                if self.x_mushroom < event.x() and self.y_mushroom < event.y() < self.y_mushroom + 50:
                    self.scene.removeItem(self.mushroom)
                    self.mushroom_alive = 0
            self.scene.removeItem(shot)

    def move_mushroom(self):
        while True:
            for i in range(35):
                self.x_mushroom = self.x_mushroom + 5
                self.mushroom_pos = self.mushroom.setPos(self.x_mushroom, self.y_mushroom)
                QtTest.QTest.qWait(100)
            for i in range(35):
                self.x_mushroom = self.x_mushroom - 5
                self.mushroom_pos = self.mushroom.setPos(self.x_mushroom, self.y_mushroom)
                QtTest.QTest.qWait(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
