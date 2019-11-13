# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from sqlite3 import Error

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from game import Ui_MainWindoow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QInputDialog
import random


class Ui_MainWindoww(QMainWindow):
    def __init__(self, players='', plaing=[]):
        super().__init__()
        self.plyers = players
        self.con = sqlite3.connect('Игры.db')
        self.win = []
        self.plaing = plaing
        self.number = 0
        self.setupUI(self)

    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.btn = QPushButton('Играть', self)
        self.btn.resize(100, 20)
        self.btn.clicked.connect(self.playing)

        self.btn1 = QPushButton('Сохранить игру', self)
        self.btn1.resize(100, 20)
        self.btn1.clicked.connect(self.save)

        MainWindow.setStatusBar(self.statusbar)

        self.lbl = QLabel(self)
        self.play = [[], [], [], []]
        self.labels = [[None for i in range(8)] for i in range(8)]
        self.lavel = 0

        if self.plaing == []:
            lenn = len(self.plyers)
            for f in range(lenn):
                name = random.choices(self.plyers)
                self.plaing.append(*name)
                a = self.plyers.pop(self.plyers.index(*name))

        if len(self.plaing) == 8:
            self.btn.move(250, 330)
            self.btn1.move(350, 330)
            self.pixmap = QPixmap('таблица.jpg')
            self.lbl.resize(600, 330)

            self.labels[self.lavel][0] = QLabel(self)
            name = self.plaing[0]
            self.labels[self.lavel][0].setText(f'{"".join(name)}')
            self.labels[self.lavel][0].move(18, 25)
            self.labels[self.lavel][0].resize(93, 24)

            self.labels[self.lavel][1] = QLabel(self)
            name = self.plaing[1]
            self.labels[self.lavel][1].setText(f'{"".join(name)}')
            self.labels[self.lavel][1].move(18, 59)
            self.labels[self.lavel][1].resize(93, 24)

            self.labels[self.lavel][2] = QLabel(self)
            name = self.plaing[2]
            self.labels[self.lavel][2].setText(f'{"".join(name)}')
            self.labels[self.lavel][2].move(18, 106)
            self.labels[self.lavel][2].resize(93, 24)

            self.labels[self.lavel][3] = QLabel(self)
            name = self.plaing[3]
            self.labels[self.lavel][3].setText(f'{"".join(name)}')
            self.labels[self.lavel][3].move(18, 139)
            self.labels[self.lavel][3].resize(93, 24)

            self.labels[self.lavel][4] = QLabel(self)
            name = self.plaing[4]
            self.labels[self.lavel][4].setText(f'{"".join(name)}')
            self.labels[self.lavel][4].move(18, 186)
            self.labels[self.lavel][4].resize(93, 24)

            self.labels[self.lavel][5] = QLabel(self)
            name = self.plaing[5]
            self.labels[self.lavel][5].setText(f'{"".join(name)}')
            self.labels[self.lavel][5].move(18, 219)
            self.labels[self.lavel][5].resize(93, 24)

            self.labels[self.lavel][6] = QLabel(self)
            name = self.plaing[6]
            self.labels[self.lavel][6].setText(f'{"".join(name)}')
            self.labels[self.lavel][6].move(18, 266)
            self.labels[self.lavel][6].resize(93, 24)

            self.labels[self.lavel][7] = QLabel(self)
            name = self.plaing[7]
            self.labels[self.lavel][7].setText(f'{"".join(name)}')
            self.labels[self.lavel][7].move(18, 299)
            self.labels[self.lavel][7].resize(93, 24)

            self.play[self.lavel] = [self.labels[self.lavel][0].text(),
                                     self.labels[self.lavel][1].text(),
                                     self.labels[self.lavel][2].text(),
                                     self.labels[self.lavel][3].text(),
                                     self.labels[self.lavel][4].text(),
                                     self.labels[self.lavel][5].text(),
                                     self.labels[self.lavel][6].text(),
                                     self.labels[self.lavel][7].text()]

            self.labels[self.lavel + 1][0] = QLabel(self)
            self.labels[self.lavel + 1][0].move(162, 39)
            self.labels[self.lavel + 1][0].resize(93, 24)

            self.labels[self.lavel + 1][1] = QLabel(self)
            self.labels[self.lavel + 1][1].move(162, 119)
            self.labels[self.lavel + 1][1].resize(93, 24)

            self.labels[self.lavel + 1][2] = QLabel(self)
            self.labels[self.lavel + 1][2].move(162, 202)
            self.labels[self.lavel + 1][2].resize(93, 24)

            self.labels[self.lavel + 1][3] = QLabel(self)
            self.labels[self.lavel + 1][3].move(162, 282)
            self.labels[self.lavel + 1][3].resize(93, 24)

            self.labels[self.lavel + 2][0] = QLabel(self)
            self.labels[self.lavel + 2][0].move(294, 79)
            self.labels[self.lavel + 2][0].resize(93, 24)

            self.labels[self.lavel + 2][1] = QLabel(self)
            self.labels[self.lavel + 2][1].move(294, 241)
            self.labels[self.lavel + 2][1].resize(93, 24)

            self.labels[self.lavel + 3][0] = QLabel(self)
            self.labels[self.lavel + 3][0].move(450, 156)
            self.labels[self.lavel + 3][0].resize(93, 24)

        elif len(self.plaing) == 4:
            self.btn.move(160, 330)
            self.btn1.move(260, 330)
            MainWindow.resize(450, 350)
            self.pixmap = QPixmap('таблица2.jpg')
            self.lbl.resize(450, 330)

            self.labels[self.lavel][0] = QLabel(self)
            name = self.plaing[0]
            self.labels[self.lavel][0].setText(f'{"".join(name)}')
            self.labels[self.lavel][0].move(12, 39)
            self.labels[self.lavel][0].resize(93, 24)

            self.labels[self.lavel][1] = QLabel(self)
            name = self.plaing[1]
            self.labels[self.lavel][1].setText(f'{"".join(name)}')
            self.labels[self.lavel][1].move(12, 119)
            self.labels[self.lavel][1].resize(93, 24)

            self.labels[self.lavel][2] = QLabel(self)
            name = self.plaing[2]
            self.labels[self.lavel][2].setText(f'{"".join(name)}')
            self.labels[self.lavel][2].move(12, 203)
            self.labels[self.lavel][2].resize(93, 24)

            self.labels[self.lavel][3] = QLabel(self)
            name = self.plaing[3]
            self.labels[self.lavel][3].setText(f'{"".join(name)}')
            self.labels[self.lavel][3].move(12, 281)
            self.labels[self.lavel][3].resize(93, 24)

            self.play[self.lavel] = [self.labels[self.lavel][0].text(),
                                     self.labels[self.lavel][1].text(),
                                     self.labels[self.lavel][2].text(),
                                     self.labels[self.lavel][3].text()]

            self.labels[self.lavel + 1][0] = QLabel(self)
            self.labels[self.lavel + 1][0].move(144, 79)
            self.labels[self.lavel + 1][0].resize(93, 24)

            self.labels[self.lavel + 1][1] = QLabel(self)
            self.labels[self.lavel + 1][1].move(144, 240)
            self.labels[self.lavel + 1][1].resize(93, 24)

            self.labels[self.lavel + 2][0] = QLabel(self)
            self.labels[self.lavel + 2][0].move(300, 155)
            self.labels[self.lavel + 2][0].resize(93, 24)

        elif len(self.plaing) == 2:
            self.btn.move(110, 330)
            self.btn1.move(210, 330)
            MainWindow.resize(320, 350)
            self.pixmap = QPixmap('таблица3.jpg')
            self.lbl.resize(320, 330)

            self.labels[self.lavel][0] = QLabel(self)
            name = self.plaing[0]
            self.labels[self.lavel][0].setText(f'{"".join(name)}')
            self.labels[self.lavel][0].move(14, 75)
            self.labels[self.lavel][0].resize(93, 24)

            self.labels[self.lavel][1] = QLabel(self)
            name = self.plaing[1]
            self.labels[self.lavel][1].setText(f'{"".join(name)}')
            self.labels[self.lavel][1].move(14, 238)
            self.labels[self.lavel][1].resize(93, 24)
            self.play[self.lavel] = [self.labels[self.lavel][0].text(),
                                     self.labels[self.lavel][1].text()]

            self.labels[self.lavel + 1][0] = QLabel(self)
            self.labels[self.lavel + 1][0].move(170, 153)
            self.labels[self.lavel + 1][0].resize(93, 24)

        self.lbl.setPixmap(self.pixmap)
        self.show()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def playing(self):
        if len(self.play[self.lavel]) == 1:
            QMessageBox.question(self, 'Finish',
                                 f'Турнир завершен',
                                 QMessageBox.Yes)
        else:
            self.number += 1
            self.hide()
            self.game = Ui_MainWindoow(self.play[self.lavel], self)

    def SendResult(self, win_players):
        self.show()
        self.lavel += 1
        self.play[self.lavel] = win_players
        for i in range(len(win_players)):
            self.labels[self.lavel][i].setText(win_players[i])
        print(win_players)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Таблица"))

    def save(self):
        if len(self.play[self.lavel]) == 1:
            QMessageBox.question(self, 'Finish',
                                 f'Турнир завершен',
                                 QMessageBox.Yes)
        else:
            flag = True
            count = 1
            i, okBtnPressed = QInputDialog.getText(self, "Введите название игры",
                                                   "Как назовём? Нельзя использовать цифры")

            for k in str(i):
                if k in '1234567890':
                    flag = False

            if flag:
                if okBtnPressed:
                    try:

                        cursorObj = self.con.cursor()

                        cursorObj.execute(
                            f"CREATE TABLE '{str(i)}'(id integer, name text, name2 text)")
                        # entities = (1, 'Andrew', 'Kirill')
                        for j in range(0, len(self.play[self.number]), 2):
                            entities = (count, self.play[self.number][j], self.play[self.number][j + 1])
                            count += 1

                            cursorObj.execute(
                                f'INSERT INTO {str(i)}(id, name, name2) VALUES(?, ?, ?)', entities)

                        self.con.commit()


                    except Error:
                        tip = QMessageBox.question(self, 'ERROR',
                                                   f'файл с таким именем уже существует. Заменить?', )

                        if tip == 16384:
                            print(1)
                            cursorObj = self.con.cursor()
                            cursorObj.execute(f'DELETE from {str(i)}')
                            for j in range(0, len(self.play[self.number]), 2):
                                entities = (
                                    count, self.play[self.number][j], self.play[self.number][j + 1])
                                count += 1

                                cursorObj.execute(
                                    f'INSERT INTO {str(i)}(id, name, name2) VALUES(?, ?, ?)', entities)

                            self.con.commit()
                        else:
                            self.save()
            else:
                QMessageBox.question(self, 'ERROR',
                                     f'Использаваны цыфры',
                                     QMessageBox.Yes)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
