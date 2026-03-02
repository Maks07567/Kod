import sys, os, pytest, tempfile, shutil,pathlib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.controller import Controller

@pytest.fixture
def ctrl(): # Фикстура, создающая контроллер с временным файлом данных
    # Создаем временную директорию для изоляции тестов
    tmp = tempfile.mkdtemp() # mkdtemp создает уникальную временную директорию
    db_file = os.path.join(tmp, "products.json") # Формируем путь к файлу данных
    db_file = os.path.normpath(db_file)  # Нормализуем путь (для Windows/Unix совместимости)
    #print("\n[DEBUG conftest] db_file =", db_file) # Закомментированный отладочный вывод

    c = Controller() # Создаем экземпляр контроллера
    c.repo.file_path = db_file # Перенаправляем репозиторий на временный файл
    # Создаем родительскую директорию для файла, если её нет
    pathlib.Path(db_file).parent.mkdir(parents=True, exist_ok=True)
    if not os.path.exists(db_file):  # Если файл не существует, создаем его с пустым списком
        c.repo._save([]) # Сохраняем пустой список

    yield c # Возвращаем контроллер для использования в тестах
    # После завершения теста выполняем очистку
    shutil.rmtree(tmp) # Удаляем временную директорию со всем содержимым




