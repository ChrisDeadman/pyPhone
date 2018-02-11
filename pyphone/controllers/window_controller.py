
from pyphone.controllers.controller import Controller


class WindowController(Controller):
    def __init__(self, panel):
        super().__init__(panel)
        panel.protocol("WM_DELETE_WINDOW", self.panel.quit)

    def exit(self):
        self.panel.destroy()
