import sys, os, pytest, tempfile, shutil,pathlib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.controller import Controller

@pytest.fixture
def ctrl():
    tmp = tempfile.mkdtemp()
    db_file = os.path.join(tmp, "products.json")
    db_file = os.path.normpath(db_file)
    #print("\n[DEBUG conftest] db_file =", db_file)

    c = Controller()
    c.repo.file_path = db_file
    pathlib.Path(db_file).parent.mkdir(parents=True, exist_ok=True)
    if not os.path.exists(db_file):
        c.repo._save([])

    yield c
    shutil.rmtree(tmp)




