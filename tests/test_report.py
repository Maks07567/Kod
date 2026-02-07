import openpyxl, os
from openpyxl.chart import PieChart

def test_report_data(ctrl):
    ctrl.add_product("Монитор", "Электроника", 10, 200)
    ctrl.add_product("Клавиатура", "Электроника", 20, 30)
    ctrl.add_product("Стол", "Мебель", 5, 100)

    data, total_qty, total_cost = ctrl.report_data()
    assert len(data) == 3
    assert total_qty == 35
    assert total_cost == 10*200 + 20*30 + 5*100

def test_excel_with_chart(ctrl):
    ctrl.add_product("Монитор", "Электроника", 5, 200)
    ctrl.add_product("Клавиатура", "Электроника", 10, 30)
    ctrl.add_product("Стол", "Мебель", 3, 100)

    from core.report_builder import build_excel
    tmp = "test_report.xlsx"
    build_excel(ctrl, tmp)

    wb = openpyxl.load_workbook(tmp)
    ws = wb.active

    assert len(ws._charts) == 1
    assert isinstance(ws._charts[0], PieChart)
    os.remove(tmp)