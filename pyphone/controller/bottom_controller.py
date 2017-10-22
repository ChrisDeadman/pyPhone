from pyphone import controller
from pyphone.controller import Controller


class BottomController(Controller):
    def __init__(self, panel):
        super().__init__(panel)

        self.panel.call_button.configure(command=lambda: controller.TopController.show_call_panel())
        self.panel.message_button.configure(command=lambda: controller.TopController.show_message_panel())
        self.panel.info_button.configure(command=lambda: controller.TopController.show_info_panel())
        self.panel.desktop_button.configure(command=lambda: controller.WindowController.exit())
