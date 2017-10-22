from tkinter import ttk
from tkinter.font import nametofont
from tkinter.ttk import Treeview


class AutosizeTreeview(Treeview):
    def insert(self, parent, index, iid=None, **kw):
        font = nametofont(ttk.Style().lookup("TTreeview", "font"))

        if "text" in kw.keys():
            self._fit_column(0, kw["text"], font)

        if "values" in kw.keys():
            column_idx = 1
            for value in kw["values"]:
                self._fit_column(column_idx, value, font)
                column_idx += 1

        return super().insert(parent, index, iid, **kw)

    def _fit_column(self, column_idx, text, font):
        column_id = "#{}".format(column_idx)
        column_width = self.column(column_id)["width"]
        text_width = font.measure(text) + 24
        if column_width < text_width:
            self.column(column_id, width=text_width)
