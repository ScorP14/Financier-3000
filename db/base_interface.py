from abc import ABC, abstractmethod

from shema import Expense


class FileDataBase(ABC):
    @abstractmethod
    def all(self) -> dict:
        ...

    @abstractmethod
    def get(self, item_id: int) -> dict:
        ...

    @abstractmethod
    def create(self, expense: Expense):
        ...

    @abstractmethod
    def update(self, item_id: int, expense: Expense) -> None:
        ...

    @abstractmethod
    def delete(self, item_id: int) -> None:
        ...



