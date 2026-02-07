import pytest

def test_add(ctrl):
    ctrl.add_product("Монитор", "Электроника", 10, 25000.5)
    data = ctrl.get_all()
    assert len(data) == 1
    assert data[0]["name"] == "Монитор"
    assert data[0]["quantity"] == 10

def test_update(ctrl):
    ctrl.add_product("Клавиатура", "Электроника", 20, 1500)
    pid = ctrl.get_all()[0]["id"]
    ctrl.update_product(pid, "Клавиатура беспроводная", "Электроника", 18, 1600)
    p = ctrl.repo.find_by_id(pid)
    assert p["name"] == "Клавиатура беспроводная"
    assert p["quantity"] == 18
    assert p["price"] == 1600

def test_delete(ctrl):
    for i in range(3):
        ctrl.add_product(f"t{i}", "кат", 1, 1)
    pid = ctrl.get_all()[1]["id"]
    ctrl.delete_product(pid)
    assert len(ctrl.get_all()) == 2
    assert ctrl.repo.find_by_id(pid) is None