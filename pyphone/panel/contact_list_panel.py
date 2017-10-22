from tkinter.ttk import Scrollbar

from pyphone.widget.autosize_tree_view import AutosizeTreeview
from pyphone.widget.panel import Panel


class ContactListPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.contacts_tree = AutosizeTreeview(self)
        self.contacts_tree.heading("#0", text="Contacts")
        self.contacts_tree.grid(row=0, column=0, sticky="nsew")

        contacts_tree_xscroll = Scrollbar(self, orient="horizontal", command=self.contacts_tree.xview)
        contacts_tree_yscroll = Scrollbar(self, orient="vertical", command=self.contacts_tree.yview)
        contacts_tree_xscroll.grid(row=1, column=0, sticky="nsew")
        contacts_tree_yscroll.grid(row=0, column=1, sticky="nsew")
        self.contacts_tree.configure(xscroll=contacts_tree_xscroll.set, yscroll=contacts_tree_yscroll.set)
