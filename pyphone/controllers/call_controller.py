import logging

from pyphone import controllers
from pyphone.controllers.controller import Controller
from pyphone.panels import *


class CallController(Controller):
    _log = logging.getLogger(__name__)

    def __init__(self, panel):
        from pyphone.controllers import GammuController, IncomingCallEvent, EndCallEvent

        super().__init__(panel)

        panel.bind_on_raise(self._on_raise)

        controllers.get(GammuController).bind(IncomingCallEvent, self._on_incoming_call)
        controllers.get(GammuController).bind(EndCallEvent, self._on_end_call)

    def _on_raise(self):
        self.show_contacts_panel()

    def _on_incoming_call(self, event):
        from pyphone.controllers import DialController
        controllers.get(DialController).set_phone_number(event.number)
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
        from pyphone.controllers import ContactsController, DialController, TopController

        phone_number = controllers.get(DialController).get_phone_number()
        contact = controllers.get(ContactsController).find_contact_by_number(phone_number)
        caller_id = phone_number if contact is None else contact.display_name
        self.panel.main_panel.IncomingCallPanel.caller_id_text.set(caller_id)

        controllers.get(TopController).show_call_panel()
        self.panel.main_panel.show_panel(IncomingCallPanel)

    def show_ongoing_call_panel(self):
        from pyphone.controllers import ContactsController, DialController, TopController

        phone_number = controllers.get(DialController).get_phone_number()
        contact = controllers.get(ContactsController).find_contact_by_number(phone_number)
        caller_id = phone_number if contact is None else contact.display_name
        self.panel.main_panel.OngoingCallPanel.caller_id_text.set(caller_id)

        controllers.get(TopController).show_call_panel()
        self.panel.main_panel.show_panel(OngoingCallPanel)

    def show_error(self, error_title, error_detail):
        from pyphone.controllers import TopController

        panel = self.panel.main_panel.ErrorPanel
        panel.error_title.configure(text=error_title)
        panel.error_detail.configure(text=error_detail)

        controllers.get(TopController).show_call_panel()
        self.panel.main_panel.show_panel(ErrorPanel)
