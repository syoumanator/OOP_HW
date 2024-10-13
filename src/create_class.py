class Category:
    """Класс описывает название категории и её описание. Подсчитывает количество
    продуктов в категории и количество категорий"""

    name = str
    description = str
    products = list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += len(products)
        Category.category_count += 1


class Product:
    """Класс описывает название продукта, назначение, цену и количество продукта"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
