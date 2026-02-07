from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QTableWidget, QTableWidgetItem, QLabel)
from PyQt5.QtCore import pyqtSignal
from windows.mixin import AutoRefreshMixin

class SearchWindow(QWidget,AutoRefreshMixin):
    closed = pyqtSignal()

    def __init__(self, controller):
        QWidget.__init__(self)
        AutoRefreshMixin.__init__(self, controller)
        self.ctrl = controller
        self.setWindowTitle("Поиск товара")
        self._build_ui()
        self._do_search()
        self.refresh()

    def _build_ui(self):
        self.name_f = QLineEdit()
        self.cat_f  = QLineEdit()
        search_btn  = QPushButton("Искать")
        back_btn    = QPushButton("Назад")
        search_btn.clicked.connect(self._do_search)
        back_btn.clicked.connect(self.closed.emit)

        top = QHBoxLayout()
        for lbl, w in (("Название", self.name_f), ("Категория", self.cat_f)):
            top.addWidget(QLabel(lbl))
            top.addWidget(w)
        top.addWidget(search_btn)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Название", "Категория", "Кол-во", "Цена", "Добавлено"])

        lo = QVBoxLayout(self)
        lo.addLayout(top)
        lo.addWidget(self.table)
        lo.addWidget(back_btn)

    def _do_search(self):
        rows = self.ctrl.search(self.name_f.text(), self.cat_f.text())
        self.table.setRowCount(len(rows))
        for r, p in enumerate(rows):
            for c, key in enumerate(
                    ["id", "name", "category", "quantity", "price", "date_added"]):
                self.table.setItem(r, c, QTableWidgetItem(str(p[key])))

    def refresh(self):
        name = self.name_f.text()
        cat  = self.cat_f.text()
        rows = self.controller.search(name, cat)
        self.table.setRowCount(len(rows))
        for r, p in enumerate(rows):
            for c, key in enumerate(
                    ["id", "name", "category", "quantity", "price", "date_added"]):
                self.table.setItem(r, c, QTableWidgetItem(str(p[key])))