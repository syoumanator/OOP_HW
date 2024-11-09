import pytest

from src.categories import Category, Product
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def category_test1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    return category1


@pytest.fixture
def empty_category():
    return Category("Пустая категория", "Категория без продуктов", [])