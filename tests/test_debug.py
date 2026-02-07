import tempfile, os, pathlib
from core.repository import ProductRepository

def test_repo_creates_file():
    tmp = tempfile.mkdtemp()
    file_path = os.path.join(tmp, "products.json")
    print("\n[DEBUG] file_path =", file_path)

    repo = ProductRepository(file_path)
    print("[DEBUG] repo.file_path =", repo.file_path)
    print("[DEBUG] folder exists :", os.path.isdir(os.path.dirname(file_path)))
    print("[DEBUG] file exists   :", os.path.exists(file_path))

    repo.add({"id": 1, "name": "Test"})
    print("[DEBUG] after add – file exists:", os.path.exists(file_path))

    os.remove(file_path)
    os.rmdir(tmp)