from pyphone.panel.contact_list_panel import ContactListPanel
from pyphone.panel.dial_panel import DialPanel
from pyphone.panel.error_panel import ErrorPanel
from pyphone.panel.gauth_panel import GAuthPanel
from pyphone.panel.incoming_call_panel import IncomingCallPanel
from pyphone.panel.ongoing_call_panel import OngoingCallPanel
from pyphone.widget.panel import Panel
from pyphone.widget.switch_panel import SwitchPanel


class CallPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=9)

        self.side_panel = SwitchPanel(self, [GAuthPanel, ContactListPanel])
        self.side_panel.grid(row=0, column=0, sticky="nsew")

        self.main_panel = SwitchPanel(self, [DialPanel, IncomingCallPanel, OngoingCallPanel, ErrorPanel])
        self.main_panel.grid(row=0, column=1, sticky="nsew")
