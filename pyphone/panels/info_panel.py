from tkinter import Label, LabelFrame
from tkinter.ttk import Progressbar, Scrollbar

from pyphone.utils import *
from pyphone.widgets import *


class InfoPanel(Panel):
    def __init__(self, master, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        system_info_frame = LabelFrame(self, text="System Information", pady=5, font=load_font(RelativeSize.normal))
        system_info_frame.grid_rowconfigure(0, weight=1)
        system_info_frame.grid_columnconfigure(0, weight=1)
        system_info_frame.grid(row=0, column=0, sticky="nsew")

        self.system_info_tree = AutosizeTreeview(system_info_frame, columns="value")
        self.system_info_tree.heading("#0", text="command")
        self.system_info_tree.column("#0", stretch=True, width=50)
        self.system_info_tree.heading("#1", text="result")
        self.system_info_tree.column("#1", stretch=True, width=50)
        self.system_info_tree.grid(row=0, column=0, sticky="nsew")

        system_info_xscroll = Scrollbar(system_info_frame, orient="horizontal",
                                        command=self.system_info_tree.xview)
        system_info_yscroll = Scrollbar(system_info_frame, orient="vertical",
                                        command=self.system_info_tree.yview)
        system_info_xscroll.grid(row=1, column=0, sticky="nsew")
        system_info_yscroll.grid(row=0, column=1, sticky="nsew")
        self.system_info_tree.configure(xscroll=system_info_xscroll.set, yscroll=system_info_yscroll.set)

        connection_status_frame = LabelFrame(self, text="Connection Status", font=load_font(RelativeSize.normal))
        connection_status_frame.grid_rowconfigure(0, weight=1)
        connection_status_frame.grid_rowconfigure(1, weight=1)
        connection_status_frame.grid_rowconfigure(2, weight=1)
        connection_status_frame.grid_columnconfigure(0, weight=1)
        connection_status_frame.grid_columnconfigure(1, weight=1)
        connection_status_frame.grid_columnconfigure(2, weight=1)
        connection_status_frame.grid(row=0, column=1, sticky="nsew")

        self.signal_status_bar = Progressbar(connection_status_frame, orient="vertical", mode="determinate")
        self.signal_status_bar.grid(row=1, column=1, sticky="nsew")
        self.signal_status_text = Label(connection_status_frame)
        self.signal_status_text.grid(row=1, column=1)

        battery_status_frame = LabelFrame(self, text="Battery Status", font=load_font(RelativeSize.normal))
        battery_status_frame.grid_rowconfigure(0, weight=1)
        battery_status_frame.grid_rowconfigure(1, weight=1)
        battery_status_frame.grid_rowconfigure(2, weight=1)
        battery_status_frame.grid_columnconfigure(0, weight=1)
        battery_status_frame.grid_columnconfigure(1, weight=1)
        battery_status_frame.grid_columnconfigure(2, weight=1)
        battery_status_frame.grid(row=0, column=2, sticky="nsew")

        self.battery_status_bar = Progressbar(battery_status_frame, orient="vertical", mode="determinate")
        self.battery_status_bar.grid(row=1, column=1, sticky="nsew")
        self.battery_status_text = Label(battery_status_frame)
        self.battery_status_text.grid(row=1, column=1)
