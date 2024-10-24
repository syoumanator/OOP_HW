import pytest

from src.categories import Category, Product


@pytest.fixture
def category():
    return Category(
        name="Телефоны детства",
        description="Вспомнить как было классно",
        products=["Nokia 3310", "Motorola", "Siemens", "Sony Ericsson"],
    )


@pytest.fixture
def product():
    return Product(name="Nokia 3310", description='Я сама "вечность"', price=9.99, quantity=1)


@pytest.fixture
def category_test():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации",
        [
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def new_product() -> dict:
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def product_1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_2():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
