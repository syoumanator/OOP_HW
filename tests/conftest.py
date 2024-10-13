import pytest

from src.create_class import Category, Product


@pytest.fixture
def category() -> object:
    return Category(
        name="Телефоны детства",
        description="Вспомнить как было классно",
        products=["Nokia 3310", "Motorola", "Siemens", "Sony Ericsson"],
    )


@pytest.fixture
def product() -> object:
    return Product(name="Nokia 3310", description='Я сама "вечность"', price=9.99, quantity=1)
