import json, os, pathlib

class ProductRepository:
    def __init__(self, file_path='data/products.json'):
        pathlib.Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        self.file_path = file_path
        if not os.path.exists(file_path):
            self._save([])

    def _load(self):
        with open(self.file_path, encoding='utf-8') as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_all(self):
        return self._load()

    def add(self, product: dict):
        data = self._load()
        data.append(product)
        self._save(data)

    def update(self, product_id: int, new_data: dict):
        data = self._load()
        for idx, p in enumerate(data):
            if p['id'] == product_id:
                data[idx] = new_data
                break
        self._save(data)

    def delete(self, product_id: int):
        data = self._load()
        data = [p for p in data if p['id'] != product_id]
        self._save(data)

    def find_by_id(self, product_id: int):
        for p in self._load():
            if p['id'] == product_id:
                return p
        return None