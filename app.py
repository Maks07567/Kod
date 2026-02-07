from PyQt5.QtWidgets import QApplication, QStackedWidget
from windows.main_menu import MainMenu
from windows.add_window      import AddWindow
from windows.browse_window   import BrowseWindow
from windows.search_window   import SearchWindow
from windows.update_window   import UpdateWindow
from windows.delete_window   import DeleteWindow
from windows.report_window   import ReportWindow
from core.controller import Controller
from style import STYLE

class AppManager(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self._init_screens()
        self.setMinimumSize(800, 600)

    def _init_screens(self):
        self.menu = MainMenu()
        self.addWidget(self.menu)

        self.addWidget(AddWindow   (self.controller))
        self.addWidget(BrowseWindow(self.controller))
        self.addWidget(SearchWindow(self.controller))
        self.addWidget(UpdateWindow(self.controller))
        self.addWidget(DeleteWindow(self.controller))
        self.addWidget(ReportWindow(self.controller))

        for idx, signal in enumerate(
            [self.menu.goto_add, self.menu.goto_browse, self.menu.goto_search,
             self.menu.goto_update, self.menu.goto_delete, self.menu.goto_report], 1):
            signal.connect(lambda *_, i=idx: self.setCurrentIndex(i))

        for i in range(1, 7):
            w = self.widget(i)
            w.closed.connect(lambda: self.setCurrentIndex(0))

        self.setCurrentIndex(0)