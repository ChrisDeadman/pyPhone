from tkinter import Frame, Label

from pyphone.utils import *
from pyphone.widgets import *


class ErrorPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        frame = Frame(self, borderwidth=2, relief="raised")
        frame.grid(row=1, column=1, sticky="nsew")
        frame.grid_rowconfigure(0, weight=2)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=2)
        frame.grid_columnconfigure(0, weight=1)

        error_image = Label(frame, image=load_image(self, "error.png", RelativeSize.big))
        error_image.grid(row=0, column=0, sticky="sew")

        self.error_title = Label(frame, font=load_font(RelativeSize.big))
        self.error_title.grid(row=1, column=0)

        self.error_detail = Label(frame)
        self.error_detail.grid(row=2, column=0)
