from base_interface import FileDataBase


class CsvFileDb(FileDataBase):
    """Сущность для работы с CSV файлами:
path_for_file: str = Путь до файла
    """
    def __init__(self, path_for_file: str) -> None:
        self.file = path_for_file
