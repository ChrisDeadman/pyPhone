from pyphone import controller
from pyphone.controller import Controller


class DialController(Controller):
    def __init__(self, panel):
        super().__init__(panel)

        panel.call_button.configure(command=self._dial_number)

    def set_phone_number(self, phone_number):
        self.panel.phone_number_text.set(phone_number)

    def get_phone_number(self):
        return self.panel.phone_number_text.get()

    def _dial_number(self):
        def command_finished(name, result, error, percents):
            if error is None:
                controller.CallController.show_ongoing_call_panel()
            else:
                controller.CallController.show_error("Could not initiate call", error)

        controller.GammuController.enqueue_command("DialVoice", (self.get_phone_number(),), command_finished)
