import sqlite3
import sys
from PyQt5.QtCore import Qt
from m_menu import Ui_MainWindow
from sqlite3 import Error
from m_table import Ui_MainWindoww
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QInputDialog, QMessageBox


class Vod:
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
            if self.lineEdit_add.text().strip():
                self.label.setText("Можно играть в 2, 4, 8")
                self.playerss.append(self.lineEdit_add.text().strip())
                self.count += 1
                event = Vod(self.lineEdit_add.text().strip())
                self.list.append(event)
                self.lineEdit_add.clear()
                self.listWidget_players.clear()
                self.listWidget_players.addItems([i.to_str() for i in self.list])
            else:
                self.label.setText('Поле пустое')
                self.lineEdit_add.clear()
        else:
            self.label.setText('Максимальное количество')
            self.add.setDisabled(True)

    def play_(self):
        if self.count == 8 or self.count == 4 or self.count == 2:
            self.hide()
            self.table = Ui_MainWindoww(self.playerss)
        else:
            self.label.setText('Недопустимое значение')

    def loading(self):
        flag = True
        flag_add = True
        sp = [[]]
        count = 0
        tbname, okBtnPressed = QInputDialog.getText(self, "Введите название игры",
                                                    "Введите названеи игры")
        for k in str(tbname):
            if k in '1234567890':
                flag = False
        if flag:
            if okBtnPressed:
                try:
                    cur = self.con.cursor()
                    cur.execute(f"Select name, name2 from {tbname}")
                    for row in cur:
                        if row[0] == '0' and row[1] == '0':
                            sp.append([])
                            count += 1
                            flag_add = False
                        if flag_add:
                            sp[count].append(row[0])
                            sp[count].append(row[1])
                        flag_add = True
                    self.table = Ui_MainWindoww(0, sp)
                    self.hide()
                except Error:
                    QMessageBox.question(self, 'ERROR',
                                         f'файл с таким именем нет',
                                         QMessageBox.Yes)
        else:
            QMessageBox.question(self, 'ERROR',
                                 f'Нельзя использовать цифры',
                                 QMessageBox.Yes)

    def keyPressEvent(self, event):
        # enter мой 16777220
        # enter котрый нужен 16777221
        if event.key() == 16777220:
            self.add_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Example()
    wnd.show()
    sys.exit(app.exec())
