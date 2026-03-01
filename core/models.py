from dataclasses import dataclass, asdict # Импортируем декоратор для датаклассов и функцию преобразования в словарь
from datetime import datetime  # Импортируем datetime для работы с датами

@dataclass
class Product:  # Класс, представляющий товар
    id: int
    name: str
    category: str
    quantity: int
    price: float
    date_added: str = None

    def __post_init__(self): # Метод, который вызывается после __init__ датакласса
        if self.date_added is None: # Если дата не была указана при создании
            self.date_added = datetime.today().strftime("%Y-%m-%d") # Устанавливаем текущую дату в формате ГГГГ-ММ-ДД

    def to_dict(self): return asdict(self) # Метод для преобразования объекта в словарь