from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
import json


class CategoryExpenseEnum(str, Enum):
    INCOME = 'доход'
    CONSUMPTION = 'расход'


@dataclass
class Expense:
    date: date
    category: CategoryExpenseEnum
    price: int
    descriptions: str
    id: int | None = field(default=None)

    def __post_init__(self):
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%Y-%m-%d').date()

    def get_list_values(self) -> list:
        return [self.date.strftime('%Y-%m-%d'), self.category.value, self.price, self.descriptions, self.id]

    def get_dict(self, get_id: bool = False) -> dict:
        data = {'date': self.date.strftime('%Y-%m-%d'), 'category': self.category,
                'price': self.price, 'descriptions': self.descriptions}
        if get_id:
            data.update({'id': self.id})
        return data

    def get_json(self) -> str:
        return json.dumps(self.get_dict(), ensure_ascii=False, indent=2)



