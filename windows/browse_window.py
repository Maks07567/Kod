from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTableWidget,
                             QTableWidgetItem, QPushButton)
from PyQt5.QtCore import pyqtSignal
from windows.mixin import AutoRefreshMixin

class BrowseWindow(QWidget, AutoRefreshMixin):
    closed = pyqtSignal()

    def __init__(self, controller):
        QWidget.__init__(self)
        AutoRefreshMixin.__init__(self, controller)

        self.setWindowTitle("Список товаров")
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Название", "Категория", "Кол-во", "Цена", "Добавлено"])
        back = QPushButton("Назад")
        back.clicked.connect(self.closed.emit)
        lo = QVBoxLayout(self)
        lo.addWidget(self.table)
        lo.addWidget(back)

    def _populate(self):
        data = self.ctrl.get_all()
        self.table.setRowCount(len(data))
        for r, p in enumerate(data):
            for c, key in enumerate(
                    ["id", "name", "category", "quantity", "price", "date_added"]):
                self.table.setItem(r, c, QTableWidgetItem(str(p[key])))
    
    def refresh(self):
        data = self.controller.get_all()
        self.table.setRowCount(len(data))
        for r, p in enumerate(data):
            for c, key in enumerate(
                    ["id", "name", "category", "quantity", "price", "date_added"]):
                self.table.setItem(r, c, QTableWidgetItem(str(p[key])))