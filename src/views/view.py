
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class View(ABC, Generic[T]):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def get_output(self) -> T | None:
        pass
