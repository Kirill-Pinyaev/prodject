# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Главное_меню.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(100, 40, 111, 31))
        self.add.setObjectName("add")
        self.lineEdit_add = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add.setGeometry(QtCore.QRect(70, 90, 171, 21))
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(65, 70, 200, 20))
        self.label.setObjectName("label")
        self.listWidget_players = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_players.setGeometry(QtCore.QRect(50, 120, 211, 211))
        self.listWidget_players.setObjectName("listWidget_players")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(104, 0, 101, 31))
        self.play.setObjectName("play")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.btn1 = QPushButton('Загрузить игру', self)
        self.btn1.resize(100, 20)
        self.btn1.move(100, 370)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.add.setText(_translate("MainWindow", "Добавить игроков"))
        self.label.setText(_translate("MainWindow", "Можно играть в 2, 4, 8"))
        self.play.setText(_translate("MainWindow", "Играть"))
