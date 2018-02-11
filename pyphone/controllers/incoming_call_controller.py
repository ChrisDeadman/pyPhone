from pyphone import controllers
from pyphone.controllers.controller import Controller


class IncomingCallController(Controller):
    def __init__(self, panel):
        super().__init__(panel)

        panel.answer_button.configure(command=self._answer_call)
        panel.decline_button.configure(command=self._decline_call)

    def _answer_call(self):
        from pyphone.controllers import CallController, GammuController

        def command_finished(name, result, error, percents):
            if error is None:
                controllers.get(CallController).show_ongoing_call_panel()
            else:
                controllers.get(CallController).show_error("Could not accept call", error)

        controllers.get(GammuController).enqueue_command("AnswerCall", (0, True), command_finished)

    def _decline_call(self):
        from pyphone.controllers import CallController, GammuController

        def command_finished(name, result, error, percents):
            if error is not None:
                controllers.get(CallController).show_error("Could not decline call", error)

        controllers.get(GammuController).enqueue_command("CancelCall", (0, True), command_finished)
