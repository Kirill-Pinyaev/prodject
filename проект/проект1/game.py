# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\student\PycharmProjects\2k19-2k20\Проект\game.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox


class Ui_MainWindoow(QMainWindow):
    def __init__(self, players, parent):
        super().__init__()
        self.Parent = parent
        self.k = 0
        self.win_players = []
        self.flag = True
        self.players = players
        self.masiv = [[None for i in range(7)] for i in range(7)]
        self.lbl = ''
        self.setupUi(self)
        self.show()

    def setupUi(self, MainWindow):
        if self.k < len(self.players):
            reply = QMessageBox.question(self, 'Игроки',
                                         f'Играют {self.players[self.k]}'
                                         f' и {self.players[self.k + 1]}',
                                         QMessageBox.Yes)
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(265, 319)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
            self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 262, 271))
            self.gridLayoutWidget.setObjectName("gridLayoutWidget")
            self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")

            for i in range(7):
                for j in range(7):
                    self.masiv[i][j] = QtWidgets.QPushButton(self.gridLayoutWidget)
                    self.masiv[i][j].setText(" ")
                    self.masiv[i][j].setObjectName(f"b_{i}_{j}")
                    self.gridLayout.addWidget(self.masiv[i][j], i, j, 1, 1)
                    self.masiv[i][j].clicked.connect(self.playing)

            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            if self.lbl == '':
                self.lbl = QLabel(self)
            self.lbl.setText(f'{self.players[self.k]} - X, {self.players[self.k + 1]} - 0')
            self.lbl.move(100, 280)
            self.lbl.resize(300, 20)
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
        else:
            self.Parent.SendResult(self.win_players)
            self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))

    def playing(self):
        if self.flag:
            self.sender().setText('X')
            self.flag = False
            self.sender().setDisabled(True)
            self.win()
        else:
            self.sender().setText('O')
            self.flag = True
            self.sender().setDisabled(True)
            self.win()

    def win(self):
        text = ''
        for i in range(7):
            for j in range(7):
                text = text + self.masiv[i][j].text()
            text += '-'
        text += '-'

        for j in range(7):
            for i in range(7):
                text = text + self.masiv[i][j].text()
            text += '-'
        text += '-'

        for i in range(7):
            text = text + self.masiv[i][i].text()
        text += '-'

        for i in range(6):
            text = text + self.masiv[i][i + 1].text()
        text += '-'

        for i in range(6):
            text = text + self.masiv[i + 1][i].text()
        text += '-'

        for i in range(5):
            text = text + self.masiv[i + 2][i].text()
        text += '-'

        for i in range(5):
            text = text + self.masiv[i][i + 2].text()
        text += '-'

        for i in range(7):
            text = text + self.masiv[6 - i][i].text()
        text += '-'

        for i in range(6):
            text = text + self.masiv[5 - i][i].text()
        text += '-'

        for i in range(6):
            text = text + self.masiv[6 - i][i + 1].text()
        text += '-'

        for i in range(5):
            text = text + self.masiv[4 - i][i].text()
        text += '-'

        for i in range(5):
            text = text + self.masiv[6 - i][i + 2].text()
        text += '-'

        if 'XXXXX' in text:
            reply = QMessageBox.question(self, 'Message',
                                         f'Выиграл {self.players[self.k]}',
                                         QMessageBox.Yes)
            for i in range(7):
                for j in range(7):
                    self.masiv[i][j].setText(' ')
                    self.flag = True
                    self.masiv[i][j].setDisabled(False)
            self.win_players.append(self.players[self.k])
            self.k += 2
            self.setupUi(self)
        elif 'OOOOO' in text:
            reply = QMessageBox.question(self, 'Message',
                                         f'Выиграл {self.players[self.k + 1]}',
                                         QMessageBox.Yes)
            for i in range(7):
                for j in range(7):
                    self.masiv[i][j].setText(' ')
                    self.flag = True
                    self.masiv[i][j].setDisabled(False)
            self.win_players.append(self.players[self.k + 1])
            self.k += 2
            self.setupUi(self)
        elif ' ' not in text:
            reply = QMessageBox.question(self, 'Message',
                                         f'Ничья - играем заново',
                                         QMessageBox.Yes)
            for i in range(7):
                for j in range(7):
                    self.masiv[i][j].setText(' ')
                    self.flag = True
                    self.masiv[i][j].setDisabled(False)
