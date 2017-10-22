import logging
import webbrowser

import httplib2
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import ClientRedirectServer, ClientRedirectHandler

_log = logging.getLogger(__name__)


def authorize(client_id, client_secret, scope, user_agent, credentials_path):
    oauth2_flow = OAuth2WebServerFlow(client_id=client_id,
                                      client_secret=client_secret,
                                      scope=scope,
                                      user_agent=user_agent)

    http = httplib2.Http(timeout=5)

    _log.info("loading credentials...")
    storage = Storage(credentials_path)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        _log.info("authorization required, requesting token...")

        try:
            # prepare response listener
            server_address = ("localhost", get_free_port())
            httpd = ClientRedirectServer(server_address, ClientRedirectHandler)
            httpd.timeout = 30

            # open authorize url
            oauth2_flow.redirect_uri = "http://{}:{}/".format(server_address[0], server_address[1])
            authorize_url = oauth2_flow.step1_get_authorize_url()
            webbrowser.open(authorize_url, new=1, autoraise=True)

            # wait for response
            httpd.handle_request()

            # handle errors
            if "code" in httpd.query_params:
                token = httpd.query_params["code"]
            elif not httpd.query_params:
                raise TimeoutError("no response from server")
            elif "error" in httpd.query_params:
                raise ConnectionRefusedError(httpd.query_params["error"])
            else:
                raise ConnectionAbortedError("server did not return authorization code")

            credentials = oauth2_flow.step2_exchange(token, http=http)
        except Exception as e:
            _log.error("authorization has failed: {0}".format(e))
            raise

        _log.info("saving credentials...")
        credentials.set_store(storage)
        storage.put(credentials)

        _log.info("authorization successful.")
    else:
        _log.info("no authorization required, using saved token...")

    return credentials.authorize(http)


def get_free_port():
    import socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(("", 0))
    free_port = socket.getsockname()[1]
    socket.close()
    return free_port
