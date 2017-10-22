from tkinter import Button, Frame, Label, StringVar

from pyphone.utils import *
from pyphone.widget.panel import Panel

_background_color = "blue"


class IncomingCallPanel(Panel):
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
        frame.grid_rowconfigure(0, weight=4)
        frame.grid_rowconfigure(1, weight=2)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        google_contacts_image = Label(frame, image=load_image(self, "person.png", RelativeSize.big))
        google_contacts_image.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.caller_id_text = StringVar(value="caller_id_text")

        caller_id_label = Label(frame, textvariable=self.caller_id_text, font=load_font(RelativeSize.big))
        caller_id_label.grid(row=1, column=0, columnspan=2, sticky="n")

        self.answer_button = Button(frame, image=load_image(self, "call.png"), relief="flat")
        self.answer_button.grid(row=2, column=0, sticky="nsew")

        self.decline_button = Button(frame, image=load_image(self, "hangup.png"), relief="flat")
        self.decline_button.grid(row=2, column=1, sticky="nsew")
