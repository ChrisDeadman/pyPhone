from pyphone.controller import *


class WindowController(Controller):
    def exit(self):
        self.panel.destroy()
