from src.product import Product


class Category:
    """Класс описывает название категории и её описание. Подсчитывает количество
    продуктов в категории и количество категорий"""

    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        """Магический метод возвращающий строковое отображение информации о количестве продуктов"""
        product_count = 0
        for product in self.__products:
            product_count += product.quantity
            print(product_count)
        return f"{self.name}, количество продуктов: {product_count} шт."

    def add_product(self, product):
        """Метод добавляет продукт к списку продуктов в категории"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Метод возвращает строку с названием продукта его стоимость и остаток"""
        products_string = ""
        for product in self.__products:
            products_string += f"{str(product)}\n"
        return products_string
