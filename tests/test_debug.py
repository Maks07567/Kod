import tempfile, os, pathlib
from core.repository import ProductRepository

def test_repo_creates_file(): # Тест создания файла репозиторием
    # Создаем временную директорию
    tmp = tempfile.mkdtemp()
    file_path = os.path.join(tmp, "products.json") # Формируем путь к файлу во временной директории
    print("\n[DEBUG] file_path =", file_path) # Отладочный вывод

    # Создаем репозиторий с указанным путем к файлу
    repo = ProductRepository(file_path)
    print("[DEBUG] repo.file_path =", repo.file_path) # Проверяем путь
    # Проверяем существование директории
    print("[DEBUG] folder exists :", os.path.isdir(os.path.dirname(file_path)))  
    # Проверяем существование файла
    print("[DEBUG] file exists   :", os.path.exists(file_path))

    # Добавляем тестовые данные
    repo.add({"id": 1, "name": "Test"})
    print("[DEBUG] after add – file exists:", os.path.exists(file_path)) # Проверяем файл

    # Очистка - удаляем созданные файлы
    os.remove(file_path) # Удаляем файл
    os.rmdir(tmp) # Удаляем временную директорию
