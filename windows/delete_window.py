from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QComboBox,
                             QPushButton, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from windows.mixin import AutoRefreshMixin

class DeleteWindow(QWidget,AutoRefreshMixin):
    closed = pyqtSignal()

    def __init__(self, controller):
        QWidget.__init__(self)
        AutoRefreshMixin.__init__(self, controller)
        self.ctrl = controller
        self.setWindowTitle("Удалить товар")
        self._build_ui()
        self._refresh_ids()
        self.refresh()

    def _build_ui(self):
        self.id_box = QComboBox()
        del_btn = QPushButton("Удалить")
        back_btn= QPushButton("Назад")
        del_btn.clicked.connect(self._delete)
        back_btn.clicked.connect(self.closed.emit)

        lo = QVBoxLayout(self)
        lo.addWidget(self.id_box)
        lo.addWidget(del_btn)
        lo.addWidget(back_btn)

    def _refresh_ids(self):
        self.id_box.clear()
        for p in self.ctrl.get_all():
            self.id_box.addItem(str(p['id']))

    def _delete(self):
        try:
            pid = int(self.id_box.currentText())
            self.ctrl.delete_product(pid)
            QMessageBox.information(self, "Успех", "Удалено")
            self._refresh_ids()
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