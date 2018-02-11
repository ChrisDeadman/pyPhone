from abc import abstractmethod

from pyphone.widgets.panel import Panel


class Keypad(Panel):
    def __init__(self, master, text_variable, cnf, **kw) -> None:
        super().__init__(master, cnf, **kw)

        for button in self.create_buttons():
            _map_button(button, text_variable)

    @abstractmethod
    def create_buttons(self):
        """Creates the buttons for this keypad."""
        return []


def _map_button(button, text_variable):
    def modify_text(button_text):
        if button_text == "ENTER":
            return text_variable.get() + "\n"
        elif button_text == "SPACE":
            return text_variable.get() + " "
        elif button_text == "BCK":
            return text_variable.get()[:-1]
        elif button_text == "CLR":
            return ""
        else:
            return text_variable.get() + button_text

    button.configure(command=lambda: text_variable.set(modify_text(button["text"])))
