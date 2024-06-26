from tabulate import tabulate

from db.csv_orm import CsvFileDb
from db.json_orm import JsonFileDb
from shema import Expense
from settings import BASE_DIR, FILE_NAME_DB_JSON, FILE_NAME_DB_CSV


def get_db(type_db: str):
    if type_db.lower() == 'json':
        return JsonFileDb(BASE_DIR / FILE_NAME_DB_JSON)
    if type_db.lower() == 'csv':
        return CsvFileDb(BASE_DIR / FILE_NAME_DB_CSV)


class PrintExpense:
    @staticmethod
    def print_list_expense(list_expense: list[Expense]) -> None:
        print(tabulate(list_expense, headers='keys', tablefmt='github', stralign='center'))
