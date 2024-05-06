import json
import os

from db.base_interface import FileDataBase


class JsonFileDb(FileDataBase):
    """Сущность для работы с JSON файлами:
path_for_file: str = Путь до файла
    """

    def __init__(self, path_for_file: str) -> None:
        self.file = path_for_file
        # Проверка на существование файла, если нет создать
        if not os.path.isfile(self.file):
            with open(self.file, 'x'):
                pass

    def create(self, expense: dict) -> None:
        """Добавляет новую запись"""
        db = self.__get_all()
        autoincrement = sorted(list(map(int, db.keys())))[-1] + 1 if len(db) != 0 else 0
        db[autoincrement] = expense
        self.write_file(db)

    def __get_all(self) -> dict:
        """Считывает весь файл"""
        with open(self.file, 'r', encoding='UTF-8') as file:
            read_file = file.read()
            return json.loads(read_file) if len(read_file) != 0 else {}

    def all(self) -> list:
        """Получить список всех записей"""
        with open(self.file, 'r', encoding='UTF-8') as file:
            read_file = file.read()
            return [value | {'id': key} for key, value in json.loads(read_file).items()] if len(read_file) != 0 else []

    def get(self, item_id: int) -> dict:
        """Получить запись по id"""
        data = self.__get_all().get(str(item_id))
        if data is None:
            raise KeyError(f'Объект c id={item_id} не найден')
        data['id'] = item_id
        return data

    def update(self, item_id: int, expense: dict) -> None:
        """Обновление записи"""
        db = self.__get_all()
        if db.get(str(item_id)) is None:
            raise KeyError(f'Объект c id={item_id} не найден')
        db[str(item_id)] = expense
        self.write_file(db)

    def delete(self, item_id: int) -> None:
        """Удаление записи"""
        db = self.__get_all()
        if not db.get(str(item_id)):
            raise KeyError(f'Объект c id={item_id} не найден')
        del db[str(item_id)]
        self.write_file(db)

    def write_file(self, data: dict) -> None:
        """Записать новые данные в файл"""
        with open(self.file, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

