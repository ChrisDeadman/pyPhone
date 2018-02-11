import threading
from datetime import datetime, timedelta

from pyphone import controllers
from pyphone.controllers.controller import Controller


class OngoingCallController(Controller):
    _start_time = datetime.now()

    def __init__(self, panel):
        super().__init__(panel)

        panel.bind_on_raise(self._on_raise)
        panel.hangup_button.configure(command=self._hangup_call)

        self._update_duration_thread = threading.Thread(target=self._update_duration_worker, daemon=True)
        self._update_duration_thread.start()

    def cleanup(self):
        super().cleanup()
        self._update_duration_thread.join()

    def _on_raise(self):
        self._start_time = datetime.now()

    def _hangup_call(self):
        from pyphone.controllers import CallController, GammuController

        def command_finished(name, result, error, percents):
            if error is not None:
                controllers.get(CallController).show_error("Could not hangup call", error)

        controllers.get(GammuController).enqueue_command("CancelCall", (0, True), command_finished)

    def _update_duration_worker(self):
        while not self.stopped.wait(0.5):
            if self.panel_visible:
                duration = timedelta(seconds=(datetime.now() - self._start_time).seconds)
                self.panel.duration_text.set(str(duration))
