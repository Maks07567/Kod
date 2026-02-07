def test_search_name(ctrl):
    ctrl.add_product("Монитор ASUS", "Электроника", 5, 200)
    ctrl.add_product("Клавиатура", "Электроника", 10, 30)
    res = ctrl.search(name="мон")
    assert len(res) == 1
    assert res[0]["name"] == "Монитор ASUS"

def test_search_category(ctrl):
    ctrl.add_product("Стол", "Мебель", 3, 100)
    ctrl.add_product("Стул", "Мебель", 4, 80)
    ctrl.add_product("Мышь", "Электроника", 15, 20)
    res = ctrl.search(category="мебель")
    assert len(res) == 2