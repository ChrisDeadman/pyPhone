from pyphone import controller
from pyphone.controller import Controller
from pyphone.panel.call_panel import CallPanel
from pyphone.panel.info_panel import InfoPanel
from pyphone.panel.message_panel import MessagePanel


class TopController(Controller):
    def show_call_panel(self):
        if self.panel.show_panel is not CallPanel:
            self.panel.show_panel(CallPanel)
            controller.CallController.show_dial_panel()

    def show_message_panel(self):
        self.panel.show_panel(MessagePanel)

    def show_info_panel(self):
        self.panel.show_panel(InfoPanel)
