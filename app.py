from datetime import datetime

from db.base_interface import FileDataBase
from shema import Expense, CategoryExpenseEnum


class App:
    def __init__(self, database: FileDataBase):
        self.__db = database

    def get_all_list_item(self) -> list[Expense]:
        """Получить все записи"""
        data = self.__db.all()
        return [Expense(**value, id=key) for key, value in data.items()]

    def get_by_item_id(self, item_id: int) -> Expense:
        """Получить запись по id"""
        data = self.__db.get(item_id)
        return Expense(**data)

    def create_item(self, expense: Expense) -> None:
        """Добавляет новую запись"""
        self.__db.create(expense.get_dict())

    def update_item(self, item_id: int, expense: Expense) -> None:
        """Обновить запись"""
        self.__db.update(item_id, expense.get_dict())

    def delete_item(self, item_id: int) -> None:
        """Удалить запись"""
        self.__db.delete(item_id)

    def get_list_item_by_category(self, category: CategoryExpenseEnum) -> list[Expense]:
        """Получить все записи"""
        data = self.__db.all()
        return [Expense(**value, id=key) for key, value in data.items() if value['category'] == category]

    def get_total_sum_category(self, category: CategoryExpenseEnum) -> int:
        """Получить сумму доходов/расходов"""
        all_items = self.__db.all()
        total_price = 0
        for key in all_items:
            if all_items[key]['category'] == category:
                total_price += all_items[key]['price']
        return total_price

    def get_current_balance(self) -> int:
        return int(self.get_total_sum_category(CategoryExpenseEnum.INCOME) -
                   self.get_total_sum_category(CategoryExpenseEnum.CONSUMPTION))

    def search_by_price(self, string_price: str) -> list[Expense]:
        """Поиск по диапазону цен"""
        start, end = map(int, string_price.split('-'))
        db = self.get_all_list_item()
        return [value for value in db if start <= int(value.price) <= end]

    def search_by_date(self, search_date_str: str) -> list[Expense]:
        """Поиск по дате"""
        db = self.get_all_list_item()
        search_date = datetime.strptime(search_date_str, '%Y-%m-%d').date()
        return [value for value in db if value.date == search_date]


class CreateExpense:
    @staticmethod
    def parse_and_valid_string_for_db(string: str) -> Expense:
        string = list(map(str.strip, string.lower().split(',')))
        if len(string) != 4:
            raise ValueError('Неверные данные')
        res = {
            'date': datetime.strptime(string[0], '%Y-%m-%d').date(),
            'category': CategoryExpenseEnum(string[1]),
            'price': int(string[2]),
            'descriptions': string[3],
        }
        return Expense(**res)


