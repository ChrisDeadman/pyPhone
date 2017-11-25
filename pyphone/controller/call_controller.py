from pyphone import controller
from pyphone.controller.gammu_controller import *
from pyphone.panel.contact_list_panel import ContactListPanel
from pyphone.panel.dial_panel import DialPanel
from pyphone.panel.error_panel import ErrorPanel
from pyphone.panel.gauth_panel import GAuthPanel
from pyphone.panel.incoming_call_panel import IncomingCallPanel
from pyphone.panel.ongoing_call_panel import OngoingCallPanel


class CallController(Controller):
    _log = logging.getLogger(__name__)

    def __init__(self, panel):
        super().__init__(panel)

        panel.bind_on_raise(self._on_raise)

        controller.GammuController.bind(IncomingCallEvent, self._on_incoming_call)
        controller.GammuController.bind(EndCallEvent, self._on_end_call)

    def _on_raise(self):
        self.show_contacts_panel()

    def _on_incoming_call(self, event):
        controller.DialController.set_phone_number(event.number)
        self.show_incoming_call_panel()

    def _on_end_call(self, _):
        self.show_dial_panel()

    def show_gauth_panel(self):
        self.panel.side_panel.show_panel(GAuthPanel)

    def show_contacts_panel(self):
        self.panel.side_panel.show_panel(ContactListPanel)

    def show_dial_panel(self):
        self.panel.main_panel.show_panel(DialPanel)

    def show_incoming_call_panel(self):
        phone_number = controller.DialController.get_phone_number()
        contact = controller.ContactsController.find_contact_by_number(phone_number)
        caller_id = phone_number if contact is None else contact.display_name
        self.panel.main_panel.IncomingCallPanel.caller_id_text.set(caller_id)

        controller.TopController.show_call_panel()
        self.panel.main_panel.show_panel(IncomingCallPanel)

    def show_ongoing_call_panel(self):
        phone_number = controller.DialController.get_phone_number()
        contact = controller.ContactsController.find_contact_by_number(phone_number)
        caller_id = phone_number if contact is None else contact.display_name
        self.panel.main_panel.OngoingCallPanel.caller_id_text.set(caller_id)

        controller.TopController.show_call_panel()
        self.panel.main_panel.show_panel(OngoingCallPanel)

    def show_error(self, error_title, error_detail):
        panel = self.panel.main_panel.ErrorPanel
        panel.error_title.configure(text=error_title)
        panel.error_detail.configure(text=error_detail)

        controller.TopController.show_call_panel()
        self.panel.main_panel.show_panel(ErrorPanel)
