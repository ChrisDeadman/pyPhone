import argparse
import logging
from tkinter import Tk
from tkinter import ttk

from oauth2client import tools

from pyphone import utils
from pyphone.controllers import *
from pyphone.panels import *


def main():
    argparser = argparse.ArgumentParser(parents=[tools.argparser])
    argparser.add_argument("--gauth-scope",
                           help="Set the scope for google api support",
                           default="https://www.googleapis.com/auth/contacts.readonly",
                           type=str)

    args = argparser.parse_args()
    config = utils.load_configuration(utils.get_user_file("pyPhone.config"))

    logging.basicConfig(filename=utils.get_user_file("pyPhone.log"), filemode="w",
                        level=getattr(logging, config["LOGGING"]["level"]),
                        format="%(asctime)s %(levelname)-5s %(name)-8s %(message)s",
                        datefmt="%H:%M:%S", )
    logging.getLogger("PIL.PngImagePlugin").setLevel("WARNING")

    try:
        window = Tk()
        window.wm_title("pyPhone v1.0.0a2")
        window.attributes("-fullscreen", True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        root = RootPanel(window)
        root.grid(sticky="nsew")

        ttk.Style().configure("TButton", background=window["background"])
        ttk.Style().configure("TProgressbar", background="green")
        ttk.Style().configure("TScrollbar", arrowsize=24)

        call_panel = root.top_panel.CallPanel

        with \
                ControllerResource(WindowController, window), \
                ControllerResource(GammuController, root), \
                ControllerResource(GAuthController, call_panel.side_panel.GAuthPanel,
                                   config["GAUTH"]["client-id"],
                                   config["GAUTH"]["client-secret"],
                                   args.gauth_scope,
                                   "pyPhone"), \
                ControllerResource(ContactsController, call_panel.side_panel.ContactListPanel), \
                ControllerResource(DialController, call_panel.main_panel.DialPanel), \
                ControllerResource(IncomingCallController, call_panel.main_panel.IncomingCallPanel), \
                ControllerResource(OngoingCallController, call_panel.main_panel.OngoingCallPanel), \
                ControllerResource(CallController, call_panel), \
                ControllerResource(InfoController, root.top_panel.InfoPanel), \
                ControllerResource(TopController, root.top_panel), \
                ControllerResource(BottomController, root.bottom_panel):
            window.mainloop()
    except Exception:
        logging.exception("Uncaught exception")
        raise


if __name__ == "__main__":
    main()
