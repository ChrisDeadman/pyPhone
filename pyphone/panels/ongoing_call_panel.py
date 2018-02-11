from tkinter import Button, Frame, Label, StringVar

from pyphone.utils import *
from pyphone.widgets import *

_background_color = "blue"


class OngoingCallPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        frame = Frame(self, borderwidth=2, relief="raised")
        frame.grid(row=1, column=1, sticky="nsew")
        frame.grid_rowconfigure(0, weight=4)
        frame.grid_rowconfigure(1, weight=2)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        google_contacts_image = Label(frame, image=load_image(self, "person.png", RelativeSize.big))
        google_contacts_image.grid(row=0, column=0, sticky="nsew")

        self.caller_id_text = StringVar(value="caller_id_text")
        self.duration_text = StringVar(value="00:00:00")

        caller_id_label = Label(frame, textvariable=self.caller_id_text, font=load_font(RelativeSize.big))
        caller_id_label.grid(row=1, column=0, sticky="n")

        duration_label = Label(frame, textvariable=self.duration_text)
        duration_label.grid(row=2, column=0, sticky="n")

        self.hangup_button = Button(frame, image=load_image(self, "hangup.png"), relief="flat")
        self.hangup_button.grid(row=3, column=0, sticky="nsew")
