from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный родительский класс"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
