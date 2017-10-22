from tkinter import Button

from pyphone.widget.keypad import Keypad


class NumKeypad(Keypad):
    buttons = []

    def __init__(self, master, text_variable, cnf={}, **kw):
        super().__init__(master, text_variable, cnf, **kw)

    def create_buttons(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.buttons.append(_assign_grid(Button(self, text="1", bg="lightgrey", relief="raised"), row=0, column=0))
        self.buttons.append(_assign_grid(Button(self, text="2", bg="lightgrey", relief="raised"), row=0, column=1))
        self.buttons.append(_assign_grid(Button(self, text="3", bg="lightgrey", relief="raised"), row=0, column=2))
        self.buttons.append(_assign_grid(Button(self, text="BCK", bg="lightgrey", relief="raised"), row=0, column=3))

        self.buttons.append(_assign_grid(Button(self, text="4", bg="lightgrey", relief="raised"), row=1, column=0))
        self.buttons.append(_assign_grid(Button(self, text="5", bg="lightgrey", relief="raised"), row=1, column=1))
        self.buttons.append(_assign_grid(Button(self, text="6", bg="lightgrey", relief="raised"), row=1, column=2))
        self.buttons.append(_assign_grid(Button(self, text="CLR", bg="lightgrey", relief="raised"), row=1, column=3))

        self.buttons.append(_assign_grid(Button(self, text="7", bg="lightgrey", relief="raised"), row=2, column=0))
        self.buttons.append(_assign_grid(Button(self, text="8", bg="lightgrey", relief="raised"), row=2, column=1))
        self.buttons.append(_assign_grid(Button(self, text="9", bg="lightgrey", relief="raised"), row=2, column=2))

        self.buttons.append(_assign_grid(Button(self, text="*", bg="lightgrey", relief="raised"), row=3, column=0))
        self.buttons.append(_assign_grid(Button(self, text="0", bg="lightgrey", relief="raised"), row=3, column=1))
        self.buttons.append(_assign_grid(Button(self, text="#", bg="lightgrey", relief="raised"), row=3, column=2))
        self.buttons.append(_assign_grid(Button(self, text="+", bg="lightgrey", relief="raised"), row=3, column=3))

        return self.buttons


def _assign_grid(widget, row, column):
    widget.grid(row=row, column=column, sticky="nsew")
    return widget
