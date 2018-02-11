from tkinter import Button, Label

from pyphone.utils import *
from pyphone.widgets import *


class GAuthPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        google_contacts_image = Label(self, image=load_image(self, "google_contacts.png", RelativeSize.big))
        google_contacts_image.grid(row=0, column=0, sticky="s")

        self.load_contacts_button = Button(self, text="Load Google Contacts")
        self.load_contacts_button.grid(row=1, column=0, sticky="n")
