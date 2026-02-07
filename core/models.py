from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    category: str
    quantity: int
    price: float
    date_added: str = None

    def __post_init__(self):
        if self.date_added is None:
            self.date_added = datetime.today().strftime("%Y-%m-%d")

    def to_dict(self): return asdict(self)