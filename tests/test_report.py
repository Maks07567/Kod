import openpyxl, os
from openpyxl.chart import PieChart

def test_report_data(ctrl): # Тест корректности данных отчета
    # Добавляем несколько товаров для теста
    ctrl.add_product("Монитор", "Электроника", 10, 200)
    ctrl.add_product("Клавиатура", "Электроника", 20, 30)
    ctrl.add_product("Стол", "Мебель", 5, 100)

    # Получаем данные отчета
    data, total_qty, total_cost = ctrl.report_data()
    assert len(data) == 3 # Проверяем количество товаров
    assert total_qty == 35 # Проверяем общее количество
    # Проверяем общую стоимость 
    assert total_cost == 10*200 + 20*30 + 5*100

def test_excel_with_chart(ctrl): # Тест создания Excel-файла с диаграммой
    # Добавляем тестовые товары
    ctrl.add_product("Монитор", "Электроника", 5, 200)
    ctrl.add_product("Клавиатура", "Электроника", 10, 30)
    ctrl.add_product("Стол", "Мебель", 3, 100)

    from core.report_builder import build_excel # Импортируем функцию построения отчета
    tmp = "test_report.xlsx" # Имя временного файла для теста
    build_excel(ctrl, tmp)  # Строим отчет и сохраняем в файл

     # Загружаем созданный файл для проверки
    wb = openpyxl.load_workbook(tmp)
    ws = wb.active # Получаем активный лист

     # Проверяем, что на листе есть диаграмма
    assert len(ws._charts) == 1 # Должна быть ровно одна диаграмма
    # Проверяем, что это круговая диаграмма
    assert isinstance(ws._charts[0], PieChart)
    os.remove(tmp) # Удаляем временный файл после теста