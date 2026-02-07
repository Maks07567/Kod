from PyQt5.QtCore import QObject

class AutoRefreshMixin(QObject):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        controller.repo_changed.connect(self.refresh)

    def refresh(self):
        raise NotImplementedError