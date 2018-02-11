from pyphone.widgets import *


class CallPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        from pyphone.panels import GAuthPanel, ContactListPanel, DialPanel, IncomingCallPanel, OngoingCallPanel, \
            ErrorPanel

        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=9)

        self.side_panel = SwitchPanel(self, [GAuthPanel, ContactListPanel])
        self.side_panel.grid(row=0, column=0, sticky="nsew")

        self.main_panel = SwitchPanel(self, [DialPanel, IncomingCallPanel, OngoingCallPanel, ErrorPanel])
        self.main_panel.grid(row=0, column=1, sticky="nsew")
