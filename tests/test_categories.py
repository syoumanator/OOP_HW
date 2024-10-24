def test_category_init(product, category) -> None:
    assert category.name == "Телефоны детства"
    assert category.description == "Вспомнить как было классно"
    category.add_product(product)
    assert category.category_count == 1
    assert category.product_count == 5


def test_category_property(category_test):
    assert category_test.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_str(category_test):
    assert str(category_test) == "Смартфоны, количество продуктов: 13 шт."
