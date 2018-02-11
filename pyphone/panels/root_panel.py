from pyphone.widgets import *


class RootPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        from pyphone.panels import CallPanel, MessagePanel, InfoPanel, BottomPanel

        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=7)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.top_panel = SwitchPanel(self, [CallPanel, MessagePanel, InfoPanel])
        self.top_panel.grid(row=0, column=0, sticky="nsew")

        self.bottom_panel = BottomPanel(self,
                                        highlightbackground="black",
                                        highlightcolor="black",
                                        highlightthickness=4,
                                        bd=0)
        self.bottom_panel.grid(row=1, column=0, sticky="nsew")
