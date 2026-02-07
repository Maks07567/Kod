import openpyxl
from openpyxl.chart import PieChart, Reference


def build_excel(controller, file_name):
    data, total_qty, total_cost = controller.report_data()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Склад"

    headers = ["ID", "Название", "Категория", "Кол-во", "Цена", "Сумма", "Добавлено"]
    ws.append(headers)
    for p in data:
        ws.append([p['id'], p['name'], p['category'],
                   p['quantity'], p['price'],
                   p['quantity'] * p['price'], p['date_added']])
    ws.append([])
    ws.append(["Итого", "", "", total_qty, "", total_cost])

    # диаграмма
    cat_qty = {}
    for p in data:
        cat = p['category']
        cat_qty[cat] = cat_qty.get(cat, 0) + p['quantity']
    chart = PieChart()
    labels = Reference(ws, min_col=3, min_row=2, max_row=1 + len(cat_qty))
    values = Reference(ws, min_col=4, min_row=2, max_row=1 + len(cat_qty))
    chart.add_data(values, titles_from_data=False)
    chart.set_categories(labels)
    chart.title = "Распределение по категориям (шт.)"
    ws.add_chart(chart, "I2")

    wb.save(file_name)