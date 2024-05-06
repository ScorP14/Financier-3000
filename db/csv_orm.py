import os
import csv

from db.base_interface import FileDataBase


class CsvFileDb(FileDataBase):
    """Сущность для работы с CSV файлами:
path_for_file: str = Путь до файла
    """

    def __init__(self, path_for_file: str) -> None:
        self.file = path_for_file
        self.__prefix = '|'
        self.headers = ('date', 'category', 'price', 'descriptions', 'id')

        self.__config_csv_dict = {
            'fieldnames': self.headers,
            'delimiter': self.__prefix,
        }

        if not os.path.isfile(self.file):
            with open(self.file, 'x', newline='') as file:
                writer = csv.DictWriter(file, **self.__config_csv_dict)

    def create(self, expense: dict) -> None:
        """Добавляет новую запись"""
        autoincrement = int(self._get_last_id_record()) + 1
        expense.update({'id': autoincrement})
        with open(self.file, 'a', encoding='UTF-8', newline='') as file:
            writer = csv.DictWriter(file, **self.__config_csv_dict)
            writer.writerow(expense)

    def _get_last_id_record(self):
        """Получить последнее id в записях"""
        with open(self.file, 'r', encoding='UTF-8', newline='') as file:
            records = csv.DictReader(file, **self.__config_csv_dict)
            list_records = list(records)
            return int(list_records[-1]['id']) if len(list_records) > 0 else 0

    def all(self) -> list:
        """Получить список всех записей"""
        with open(self.file, encoding='UTF-8', newline='') as file:
            reader = csv.DictReader(file, **self.__config_csv_dict)
            list_data = list(reader)
            if len(list_data) > 0:
                return list_data
            return []

    def get(self, item_id: int) -> dict:
        """Получить запись по id"""
        data = self.all()
        for row in data:
            if row['id'] == str(item_id):
                return row
        raise KeyError(f'Объект c id={item_id} не найден')

    def update(self, item_id: int, expense: dict) -> None:
        """Обновление записи"""
        data = self.all()
        for index, row in enumerate(data):
            if row['id'] == str(item_id):
                data[index] = expense
                data[index]['id'] = str(item_id)
                with open(self.file, 'w', encoding='UTF-8', newline='') as file:
                    writer = csv.DictWriter(file, **self.__config_csv_dict)
                    writer.writerows(data)
                return
        raise KeyError(f'Объект c id={item_id} не найден')

    def delete(self, item_id: int) -> None:
        """Удаление записи"""
        data = self.all()
        for index, row in enumerate(data):
            if row['id'] == str(item_id):
                del data[index]
                with open(self.file, 'w', encoding='UTF-8', newline='') as file:
                    writer = csv.DictWriter(file, **self.__config_csv_dict)
                    writer.writerows(data)
                return
        raise KeyError(f'Объект c id={item_id} не найден')


