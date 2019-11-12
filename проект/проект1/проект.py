import sqlite3
import sys
from PyQt5.QtCore import Qt
from m_menu import Ui_MainWindow
from sqlite3 import Error
from m__table import Ui_MainWindoww
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QInputDialog, QMessageBox


class Diary:
    def __init__(self, name):
        self.name = name

    def to_str(self):
        return f'{self.name}'

    def __str__(self):
        return self.to_str()


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 0
        self.con = sqlite3.connect('Игры.db')
        self.add.clicked.connect(self.add_)
        self.btn1.clicked.connect(self.loading)
        self.list = []
        self.playerss = []
        self.play.clicked.connect(self.play_)
        self.current = ''

    def add_(self):
        if self.count < 8:
            if self.lineEdit_add.text():
                self.label.setText("Возможно 8 или 4 или 2 игрока")
                self.playerss.append(self.lineEdit_add.text())
                self.count += 1
                event = Diary(self.lineEdit_add.text())
                self.list.append(event)
                self.lineEdit_add.clear()
                self.listWidget_players.clear()
                self.listWidget_players.addItems([i.to_str() for i in self.list])
            else:
                self.label.setText('Поле пустое')
        else:
            self.label.setText('Максимальное количество')
            self.add.setDisabled(True)

    def play_(self):
        if self.count == 8 or self.count == 4 or self.count == 2:
            self.hide()
            self.table = Ui_MainWindoww(self.playerss)
        else:
            self.label.setText('Недопустимое значение')

    def play_2(self, win):
        self.table = Ui_MainWindoww(self.playerss)

    def loading(self):
        flag = True
        sp = []
        tbname, okBtnPressed = QInputDialog.getText(self, "Введите название игры",
                                                    "Введите названеи игры")
        for k in str(tbname):
            if k in '1234567890':
                flag = False
        if flag and okBtnPressed:
            try:
                cur = self.con.cursor()
                cur.execute(f"Select name, name2 from {tbname}")
                for row in cur:
                    print(row)
                    sp.append(row[0])
                    sp.append(row[1])
                self.table = Ui_MainWindoww(0, sp)
                self.hide()
            except Error:
                QMessageBox.question(self, 'ERROR',
                                     f'файл с таким именем нет',
                                     QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Example()
    wnd.show()
    sys.exit(app.exec())
