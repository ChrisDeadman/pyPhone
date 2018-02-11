from pyphone import controllers
from pyphone.controllers.controller import Controller
from pyphone.panels import *


class TopController(Controller):
    def show_call_panel(self):
        from pyphone.controllers import CallController

        if self.panel.show_panel is not CallPanel:
            self.panel.show_panel(CallPanel)
            controllers.get(CallController).show_dial_panel()

    def show_message_panel(self):
        self.panel.show_panel(MessagePanel)

    def show_info_panel(self):
        self.panel.show_panel(InfoPanel)
