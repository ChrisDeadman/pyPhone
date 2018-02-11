import threading


class Controller:
    def __init__(self, panel):
        self.panel = panel
        self.panel_visible = False
        self.stopped = threading.Event()

        if self.panel is not None:
            self.panel.bind("<Visibility>", self._on_panel_visibility_changed)

    def cleanup(self):
        self.stopped.set()

    def _on_panel_visibility_changed(self, event):
        self.panel_visible = (event.state != "VisibilityFullyObscured")
