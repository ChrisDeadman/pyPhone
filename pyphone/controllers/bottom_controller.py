from pyphone import controllers
from pyphone.controllers.controller import Controller


class BottomController(Controller):
    def __init__(self, panel):
        from pyphone.controllers import TopController, WindowController

        super().__init__(panel)

        self.panel.call_button.configure(command=lambda: controllers.get(TopController).show_call_panel())
        self.panel.message_button.configure(command=lambda: controllers.get(TopController).show_message_panel())
        self.panel.info_button.configure(command=lambda: controllers.get(TopController).show_info_panel())
        self.panel.desktop_button.configure(command=lambda: controllers.get(WindowController).exit())
