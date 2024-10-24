class Product:
    """Класс описывает название продукта, назначение, цену и количество продукта"""

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Магический метод возвращающий строковое отображение информации о стоимости и количестве продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод возвращает сумму цен двух товаров"""
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, dict_product: dict, products=None):
        if products:
            for product in products:
                if product.name == dict_product["name"]:
                    product.quantity += dict_product["quantity"]
                    product.price = max([product.price, product["price"]])
        return cls(**dict_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод позволяет изменить цену продукта"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(f"Подтвердите понижение цены c {self.__price} до {new_price}: y(да)/n(нет)\n").lower()
            if confirmation == "y":
                self.__price = new_price
        else:
            self.__price = new_price
