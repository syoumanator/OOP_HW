def test_category_init(product, category) -> None:
    assert product.name == "Nokia 3310"
    assert product.description == 'Я сама "вечность"'
    assert product.price == 9.99
    assert product.quantity == 1

    assert category.name == "Телефоны детства"
    assert category.description == "Вспомнить как было классно"
    assert category.products == ["Nokia 3310", "Motorola", "Siemens", "Sony Ericsson"]

    assert category.category_count == 1
    assert category.product_count == 4
