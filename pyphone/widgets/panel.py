import logging
from tkinter import Frame


class Panel(Frame):
    _log = logging.getLogger(__name__)

    _on_raise = None

    def __init__(self, master, cnf, **kw):
        super().__init__(master, cnf, **kw)

    def bind_on_raise(self, callback):
        self._on_raise = callback

    def tkraise(self, above_this=None):
        super().tkraise(above_this)
        self._log.debug("{}: tkraise()".format(type(self).__name__))

        if self._on_raise is not None:
            self._on_raise()
