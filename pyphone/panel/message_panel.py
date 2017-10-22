from tkinter import Label

from pyphone.utils import *
from pyphone.widget.panel import Panel


class MessagePanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = Label(self, text="not implemented yet :-(", font=load_font(RelativeSize.big))
        self.title_label.grid()
