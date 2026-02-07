from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton,
                             QLabel, QMessageBox)
from PyQt5.QtCore import pyqtSignal

class AddWindow(QWidget):
    closed = pyqtSignal()

    def __init__(self, controller):
        super().__init__()
        self.ctrl = controller
        self.setWindowTitle("Добавить товар")
        self._build_ui()

    def _build_ui(self):
        self.name   = QLineEdit()
        self.cat    = QLineEdit()
        self.qty    = QLineEdit()
        self.price  = QLineEdit()

        save_btn = QPushButton("Сохранить")
        back_btn = QPushButton("Назад")
        save_btn.clicked.connect(self._save)
        back_btn.clicked.connect(self.closed.emit)

        lo = QVBoxLayout(self)
        for lbl, widget in (("Название", self.name),
                            ("Категория", self.cat),
                            ("Количество", self.qty),
                            ("Цена", self.price)):
            lo.addWidget(QLabel(lbl))
            lo.addWidget(widget)
        lo.addWidget(save_btn)
        lo.addWidget(back_btn)

    def _save(self):
        try:
            self.ctrl.add_product(self.name.text(),
                                  self.cat.text(),
                                  self.qty.text(),
                                  self.price.text())
            QMessageBox.information(self, "Успех", "Товар добавлен")
            for w in (self.name, self.cat, self.qty, self.price):
                w.clear()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))