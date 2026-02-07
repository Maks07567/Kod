import sys
from PyQt5.QtWidgets import QApplication
from app import AppManager
from style import STYLE

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    win = AppManager()
    win.show()
    sys.exit(app.exec_())