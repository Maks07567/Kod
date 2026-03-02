import pytest

def test_add(ctrl): # Тест добавления товара
    # Вызываем метод добавления товара с тестовыми данными
    ctrl.add_product("Монитор", "Электроника", 10, 25000.5)
    data = ctrl.get_all() # Получаем все товары
    assert len(data) == 1 # Проверяем, что добавился ровно 1 товар
    assert data[0]["name"] == "Монитор" # Проверяем название товара
    assert data[0]["quantity"] == 10 # Проверяем количество товара

def test_update(ctrl): # Тест обновления товара
    # Сначала добавляем товар
    ctrl.add_product("Клавиатура", "Электроника", 20, 1500)
    pid = ctrl.get_all()[0]["id"] # Получаем ID добавленного товара
    # Обновляем товар с новыми данными
    ctrl.update_product(pid, "Клавиатура беспроводная", "Электроника", 18, 1600)
    p = ctrl.repo.find_by_id(pid) # Ищем товар по ID в репозитории
    assert p["name"] == "Клавиатура беспроводная" # Проверяем обновленное название
    assert p["quantity"] == 18 # Проверяем обновленное количество
    assert p["price"] == 1600 # Проверяем обновленную цену

def test_delete(ctrl): # Тест удаления товара
    # Добавляем 3 товара в цикле
    for i in range(3):
        ctrl.add_product(f"t{i}", "кат", 1, 1) # f"t{i}" создает строки "t0", "t1", "t2"
    pid = ctrl.get_all()[1]["id"]  # Получаем ID второго товара 
    ctrl.delete_product(pid) # Удаляем товар по ID
    assert len(ctrl.get_all()) == 2 # Проверяем, что осталось 2 товара
    # Проверяем, что удаленный товар больше не найден
    assert ctrl.repo.find_by_id(pid) is None