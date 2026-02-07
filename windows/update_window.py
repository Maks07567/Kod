from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QComboBox, QLineEdit,
                             QPushButton, QLabel, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from windows.mixin import AutoRefreshMixin

class UpdateWindow(QWidget,AutoRefreshMixin):
    closed = pyqtSignal()

    def __init__(self, controller):
        QWidget.__init__(self)
        AutoRefreshMixin.__init__(self, controller)
        self.ctrl = controller
        self.setWindowTitle("Обновить товар")
        self._build_ui()
        self._fill_ids()
        self.refresh()

    def _build_ui(self):
        self.id_box = QComboBox()
        self.name   = QLineEdit()
        self.cat    = QLineEdit()
        self.qty    = QLineEdit()
        self.price  = QLineEdit()

        self.id_box.currentTextChanged.connect(self._load_values)

        update_btn = QPushButton("Обновить")
        back_btn   = QPushButton("Назад")
        update_btn.clicked.connect(self._update)
        back_btn.clicked.connect(self.closed.emit)

        lo = QVBoxLayout(self)
        lo.addWidget(QLabel("ID товара"))
        lo.addWidget(self.id_box)
        for lbl, w in (("Название", self.name),
                       ("Категория", self.cat),
                       ("Количество", self.qty),
                       ("Цена", self.price)):
            lo.addWidget(QLabel(lbl))
            lo.addWidget(w)
        lo.addWidget(update_btn)
        lo.addWidget(back_btn)

    def _fill_ids(self):
        self.id_box.clear()
        for p in self.ctrl.get_all():
            self.id_box.addItem(str(p['id']))

    def _load_values(self):
        pid = self._current_id()
        if not pid: return
        p = self.ctrl.repo.find_by_id(pid)
        if p:
            self.name.setText(p['name'])
            self.cat.setText(p['category'])
            self.qty.setText(str(p['quantity']))
            self.price.setText(str(p['price']))

    def _current_id(self):
        try:
            return int(self.id_box.currentText())
        except:
            return None

    def _update(self):
        try:
            pid = self._current_id()
            if not pid:
                return
            self.ctrl.update_product(pid, self.name.text(),
                                     self.cat.text(),
                                     self.qty.text(),
                                     self.price.text())
            QMessageBox.information(self, "Успех", "Обновлено")
            self._fill_ids()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))
    
    def refresh(self):
        current = self.id_box.currentText()
        self.id_box.clear()
        for p in self.controller.get_all():
            self.id_box.addItem(str(p['id']))
        idx = self.id_box.findText(current)
        if idx >= 0:
            self.id_box.setCurrentIndex(idx)
        self._load_values()