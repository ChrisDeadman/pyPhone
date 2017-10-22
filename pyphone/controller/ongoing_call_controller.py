from datetime import datetime, timedelta

from pyphone.controller import *


class OngoingCallController(Controller):
    _start_time = datetime.now()

    def __init__(self, panel):
        super().__init__(panel)

        panel.bind_on_raise(self._on_raise)

        self._update_duration_thread = threading.Thread(target=self._update_duration_worker)
        self._update_duration_thread.start()

    def _on_raise(self):
        self._start_time = datetime.now()

    def cleanup(self):
        super().cleanup()
        self._update_duration_thread.join()

    def _update_duration_worker(self):
        while not self.stopped.wait(0.5):
            if self.panel_visible:
                duration = timedelta(seconds=(datetime.now() - self._start_time).seconds)
                self.panel.duration_text.set(str(duration))
