from pyphone import controller
from pyphone.controller.gammu_controller import *


class IncomingCallController(Controller):
    def __init__(self, panel):
        super().__init__(panel)

        panel.answer_button.configure(command=self._answer_call)
        panel.decline_button.configure(command=self._decline_call)

    def _answer_call(self):
        def command_finished(name, result, error, percents):
            if error is None:
                controller.CallController.show_ongoing_call_panel()
            else:
                controller.CallController.show_error("Could not accept call", error)

        controller.GammuController.enqueue_command("AnswerCall", (0, True), command_finished)

    def _decline_call(self):
        def command_finished(name, result, error, percents):
            if error is not None:
                controller.CallController.show_error("Could not decline call", error)

        controller.GammuController.enqueue_command("CancelCall", (0, True), command_finished)
