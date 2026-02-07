from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy)
from PyQt5.QtCore import pyqtSignal

class MainMenu(QWidget):
    goto_add      = pyqtSignal()
    goto_browse   = pyqtSignal()
    goto_search   = pyqtSignal()
    goto_update   = pyqtSignal()
    goto_delete   = pyqtSignal()
    goto_report   = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система управления складом – Главное меню")
        self._build_ui()

    def _build_ui(self):
        label = QLabel("Выберите действие")
        label.setStyleSheet("font-size:16pt; margin-bottom:10px;")

        buttons = [
            ("Добавление товара",     self.goto_add),
            ("Просмотр всего содержимого", self.goto_browse),
            ("Найти товар",           self.goto_search),
            ("Обновить товар",        self.goto_update),
            ("Удалить товар",         self.goto_delete),
            ("Сформировать отчёт",    self.goto_report),
        ]

        lo = QVBoxLayout()
        lo.addWidget(label)
        for text, signal in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(signal.emit)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            lo.addWidget(btn)
        self.setLayout(lo)
        self.resize(320, 400)