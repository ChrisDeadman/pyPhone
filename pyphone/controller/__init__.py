import sys
import threading


class ControllerResource:
    def __init__(self, controller_type, panel, *args):
        self._controller_type = controller_type
        self._panel = panel
        self._kwargs = args

    def __enter__(self):
        self.package_obj = self._controller_type(self._panel, *self._kwargs)
        setattr(sys.modules[__name__], self._controller_type.__name__, self.package_obj)
        return self.package_obj

    def __exit__(self, exc_type, exc_value, traceback):
        self.package_obj.cleanup()


class Controller:
    panel_visible = False
    stopped = threading.Event()

    def __init__(self, panel):
        self.panel = panel
        self.panel.bind("<Visibility>", self._on_panel_visibility_changed)

    def cleanup(self):
        self.stopped.set()

    def _on_panel_visibility_changed(self, event):
        self.panel_visible = (event.state != "VisibilityFullyObscured")
