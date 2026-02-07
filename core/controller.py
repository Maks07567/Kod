from .models import Product
from .repository import ProductRepository
from PyQt5.QtCore import QObject, pyqtSignal

class Controller(QObject):
    repo_changed = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.repo = ProductRepository()

    def _next_id(self):
        ids = [p['id'] for p in self.repo.get_all()]
        return max(ids, default=0) + 1

    def add_product(self, name, category, quantity, price):
        p = Product(id=self._next_id(),
                    name=name.strip(),
                    category=category.strip(),
                    quantity=int(quantity),
                    price=float(price))
        self.repo.add(p.to_dict())
        self.repo_changed.emit()

    def get_all(self):
        return self.repo.get_all()

    def search(self, name='', category=''):
        name, category = name.lower(), category.lower()
        return [p for p in self.get_all()
                if name in p['name'].lower() and category in p['category'].lower()]

    def update_product(self, pid, name, category, quantity, price):
        self.repo.update(pid,
                         Product(id=pid, name=name, category=category,
                                 quantity=int(quantity), price=float(price)).to_dict())
        self.repo_changed.emit()

    def delete_product(self, pid):
        self.repo.delete(pid)
        self.repo_changed.emit()

    def report_data(self):
        data = self.get_all()
        total_qty = sum(p['quantity'] for p in data)
        total_cost = sum(p['quantity'] * p['price'] for p in data)
        return data, total_qty, total_cost