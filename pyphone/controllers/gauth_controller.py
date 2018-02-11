import logging
import threading

from apiclient.discovery import build

from pyphone import oauth2_flow, controllers
from pyphone.controllers.controller import Controller
from pyphone.utils import get_user_file

_credentials_path = get_user_file("google-credentials.dat")


class GAuthController(Controller):
    _log = logging.getLogger(__name__)

    _authorize_thread = None

    people_service = None

    def __init__(self, panel, client_id, client_secret, scope, user_agent):
        super().__init__(panel)

        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope
        self._user_agent = user_agent

        panel.load_contacts_button.configure(command=self._authorize)

    def cleanup(self):
        super().cleanup()
        if self._authorize_thread is not None:
            self._authorize_thread.join()

    def _authorize(self):
        self.panel.load_contacts_button.configure(state="disabled")
        self._authorize_thread = threading.Thread(target=self._authorize_worker, daemon=True)
        self._authorize_thread.start()

    def _authorize_worker(self):
        from pyphone.controllers import CallController

        try:
            if self._client_id is None or self._client_secret is None:
                raise ValueError("client_id and/or client_secret not set")

            http = oauth2_flow.authorize(self._client_id,
                                         self._client_secret,
                                         self._scope,
                                         self._user_agent,
                                         _credentials_path)

            self.people_service = build("people", "v1", http=http, cache_discovery=False)
        except Exception as e:
            error_message = "{}: {}".format(type(e).__name__, e)
            self._log.error("authorization failed: {}".format(error_message))
            controllers.get(CallController).show_error("Authorization failed", error_message)

        self.panel.load_contacts_button.configure(state="normal")
        controllers.get(CallController).show_contacts_panel()
