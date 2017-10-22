from pyphone.widget.panel import Panel


class SwitchPanel(Panel):
    shown_panel = None

    def __init__(self, master, panel_types, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for panel_type in panel_types:
            self.add_panel(panel_type)

    def add_panel(self, panel_type):
        panel = panel_type(self)
        panel.grid(row=0, column=0, sticky="nsew")
        setattr(self, panel_type.__name__, panel)

    def show_panel(self, panel_type):
        panel = getattr(self, panel_type.__name__)
        if self.shown_panel != panel:
            self.shown_panel = panel
            panel.tkraise()
