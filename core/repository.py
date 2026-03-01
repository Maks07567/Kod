import json, os, pathlib 

class ProductRepository:  # Класс для хранения и получения данных о товарах
    def __init__(self, file_path='data/products.json'): # Конструктор с путем к файлу по умолчанию
        pathlib.Path(file_path).parent.mkdir(parents=True, exist_ok=True) # Создаем директорию для файла, если её нет 
        self.file_path = file_path # Сохраняем путь к файлу
        if not os.path.exists(file_path): # Если файл не существует
            self._save([])  # Создаем его с пустым списком

    def _load(self):  # Приватный метод загрузки данных из файла
        with open(self.file_path, encoding='utf-8') as f:
            return json.load(f)

    def _save(self, data): # Приватный метод сохранения данных в файл
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_all(self): # Метод получения всех товаров
        return self._load()  # Загружаем и возвращаем все данные

    def add(self, product: dict): # Метод добавления нового товара
        data = self._load()
        data.append(product)
        self._save(data)

    def update(self, product_id: int, new_data: dict): # Метод обновления товара по ID
        data = self._load()
        for idx, p in enumerate(data):
            if p['id'] == product_id: # Проходим по всем товарам с индексом
                data[idx] = new_data
                break
        self._save(data)

    def delete(self, product_id: int): # Метод удаления товара по ID
        data = self._load()
        data = [p for p in data if p['id'] != product_id] # Оставляем только товары с ID не равным удаляемому
        self._save(data)

    def find_by_id(self, product_id: int):# Метод поиска товара по ID
        for p in self._load():
            if p['id'] == product_id:
                return p
        return None