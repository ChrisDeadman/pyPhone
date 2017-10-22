from tkinter import Button

from pyphone.utils import *
from pyphone.widget.panel import Panel


class BottomPanel(Panel):
    _images = []

    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        for column in range(0, 4):
            self.grid_columnconfigure(column, weight=1)

        self.call_button = Button(self, image=load_image(self, "call.png", RelativeSize.big), relief="flat")
        self.call_button.grid(row=0, column=0, sticky="nsew")

        self.message_button = Button(self, image=load_image(self, "message.png", RelativeSize.big), relief="flat")
        self.message_button.grid(row=0, column=1, sticky="nsew")

        self.info_button = Button(self, image=load_image(self, "info.png", RelativeSize.big), relief="flat")
        self.info_button.grid(row=0, column=2, sticky="nsew")

        self.desktop_button = Button(self, image=load_image(self, "desktop.png", RelativeSize.big), relief="flat")
        self.desktop_button.grid(row=0, column=3, sticky="nsew")
