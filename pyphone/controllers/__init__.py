from pyphone.controllers.bottom_controller import BottomController
from pyphone.controllers.call_controller import CallController
from pyphone.controllers.contacts_controller import ContactsController
from pyphone.controllers.dial_controller import DialController
from pyphone.controllers.gammu_controller import GammuController, IncomingCallEvent, EndCallEvent
from pyphone.controllers.gauth_controller import GAuthController
from pyphone.controllers.incoming_call_controller import IncomingCallController
from pyphone.controllers.info_controller import InfoController
from pyphone.controllers.ongoing_call_controller import OngoingCallController
from pyphone.controllers.top_controller import TopController
from pyphone.controllers.window_controller import WindowController

_controller_instances = {}


class ControllerResource:
    def __init__(self, controller_type, panel, *args):
        self._controller_type = controller_type
        self._panel = panel
        self._kwargs = args

    def __enter__(self):
        self.package_obj = self._controller_type(self._panel, *self._kwargs)
        _controller_instances[self._controller_type] = self.package_obj
        return self.package_obj

    def __exit__(self, exc_type, exc_value, traceback):
        self.package_obj.cleanup()


def get(controller_type):
    return _controller_instances[controller_type]
