import openpyxl # Импортируем библиотеку для работы с Excel
from openpyxl.chart import PieChart, Reference # Импортируем классы для создания круговой диаграммы


def build_excel(controller, file_name): # Функция построения Excel-отчета
    data, total_qty, total_cost = controller.report_data() # Получаем данные из контроллера
    wb = openpyxl.Workbook() # Создаем новую рабочую книгу Excel
    ws = wb.active
    ws.title = "Склад"

    headers = ["ID", "Название", "Категория", "Кол-во", "Цена", "Сумма", "Добавлено"] # Заголовки столбцов
    ws.append(headers) # Добавляем заголовки в первую строку
    for p in data: # Для каждого товара в данных
        ws.append([p['id'], p['name'], p['category'],  # Добавляем строку с данными товара
                   p['quantity'], p['price'],
                   p['quantity'] * p['price'], p['date_added']]) # Считаем сумму (кол-во * цена)
    ws.append([])
    ws.append(["Итого", "", "", total_qty, "", total_cost]) # Добавляем строку с итогами

    # диаграмма
    cat_qty = {} # Словарь для подсчета количества по категориям
    for p in data: # Для каждого товара
        cat = p['category'] # Получаем категорию
        cat_qty[cat] = cat_qty.get(cat, 0) + p['quantity'] # Увеличиваем счетчик для этой категории
    chart = PieChart()  # Создаем объект круговой диаграммы
    labels = Reference(ws, min_col=3, min_row=2, max_row=1 + len(cat_qty)) # Диапазон с названиями категорий (столбец C)
    values = Reference(ws, min_col=4, min_row=2, max_row=1 + len(cat_qty)) # Диапазон с количествами (столбец D)
    chart.add_data(values, titles_from_data=False) # Добавляем данные в диаграмму
    chart.set_categories(labels) # Устанавливаем подписи категорий
    chart.title = "Распределение по категориям (шт.)"
    ws.add_chart(chart, "I2") # Добавляем диаграмму на лист, начиная с ячейки I2

    wb.save(file_name) # Сохраняем файл Excel