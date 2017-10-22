from tkinter import Button, Entry, Frame, StringVar

from pyphone.utils import *
from pyphone.widget.num_keypad import NumKeypad
from pyphone.widget.panel import Panel


class DialPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=8)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=1)

        self.phone_number_text = StringVar()

        number_grid = Frame(self, borderwidth=2, relief="raised")
        number_grid.grid_rowconfigure(0, weight=1)
        number_grid.grid_columnconfigure(0, weight=4)
        number_grid.grid_columnconfigure(1, weight=1)
        number_grid.grid(row=1, column=1, sticky="nsew")

        phone_number_entry = Entry(number_grid, textvariable=self.phone_number_text, font=load_font(RelativeSize.big))
        phone_number_entry.grid(row=0, column=0, sticky="nsew")

        self.call_button = Button(number_grid, image=load_image(self, "call.png"), relief="flat")
        self.call_button.grid(row=0, column=1, sticky="nsew")

        self.dial_pad = NumKeypad(self, self.phone_number_text)
        self.dial_pad.grid(row=3, column=1, sticky="nsew")
