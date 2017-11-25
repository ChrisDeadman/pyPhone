import logging
from collections import namedtuple

from gammu import StateMachine
from gammu.worker import GammuWorker

from pyphone.controller import *

IncomingCallEvent = namedtuple("IncomingCallEvent", ["number"])
EndCallEvent = namedtuple("EndCallEvent", ["number"])


class GammuController(Controller):
    _log = logging.getLogger(__name__)

    _system_callbacks = {}
    _user_callbacks = {}

    connecting = threading.Event()
    connected = threading.Event()
    ongoing_call = threading.Event()

    def __init__(self, root_panel):
        super().__init__(root_panel)

        self._system_callbacks = {"Init": self._on_init_complete,
                                  "DialVoice": self._on_dial_voice_complete,
                                  "AnswerCall": self._on_answer_call_complete}

        self._state_machine = StateMachine()
        self._gammu_worker = GammuWorker(self._on_gammu_result)
        self._reconnect_thread = threading.Thread(target=self._reconnect_worker)
        self._reconnect_thread.start()

    def _reconnect_worker(self):
        running = True
        while running:
            if not self.connecting.isSet():
                if not self.connected.isSet():
                    self.try_connect()
                else:
                    # necessary for incoming notifications to work correctly
                    self.enqueue_command("ReadDevice")
            running = not self.stopped.wait(2)

    def try_connect(self):
        self.connecting.set()
        if self._gammu_worker._thread is not None:
            self._gammu_worker.terminate()
        self._state_machine.ReadConfig()
        self._gammu_worker.configure(self._state_machine.GetConfig())
        self._log.debug("connecting...")
        self._gammu_worker.initiate()

    def cleanup(self):
        super().cleanup()
        self._disconnect()

    def enqueue_command(self, command, params=None, callback=None):
        self._log.debug("-> [command={}] [params={}]".format(command, params))

        if not self.connected.wait(timeout=5):
            if callback is not None:
                self._log.error("<- ERR_NOTCONNECTED: ({} {})".format(command, params))
                callback(command, None, "ERR_NOTCONNECTED", 100)
            return

        if callback is not None:
            self._user_callbacks[command] = callback

        self._gammu_worker.enqueue_command(command, params)

    def bind(self, event, callback):
        self._user_callbacks[event] = callback

    def _disconnect(self):
        try:
            if self._gammu_worker._thread is not None:
                self._log.info("disconnecting...")
                self._gammu_worker.terminate()
        except:
            pass
        self.connected.clear()

    def _on_gammu_result(self, name, result, error, percents):
        if self.stopped.isSet():
            return

        if error == "ERR_NONE":
            error = None

        self._log.debug("<- {0} ({1:d}%): \"{2}\"".format(name, percents, result if error is None else error))

        if name in self._system_callbacks.keys():
            self._system_callbacks[name](name, result, error, percents)

        if name in self._user_callbacks.keys():
            self._user_callbacks[name](name, result, error, percents)

        if (error is not None) and (error.startswith("ERR_DEVICE")):
            self._disconnect()

    def _on_init_complete(self, name, result, error, percents):
        if error is None:
            self._log.info("connected!")
            self.connected.set()
            self.connecting.clear()

            self._gammu_worker.enqueue_command("SetIncomingCall", (True,))
            self._gammu_worker.enqueue_command("SetIncomingCallback", (self._on_incoming_call,))

            self._gammu_worker.enqueue_command("SetIncomingSMS", (True,))
            self._gammu_worker.enqueue_command("SetIncomingCallback", (self._on_incoming_sms,))

            self._gammu_worker.enqueue_command("SetIncomingUSSD", (True,))
            self._gammu_worker.enqueue_command("SetIncomingCallback", (self._on_incoming_ussd,))
        else:
            self._log.error("connection failed: {}".format(error))
            self.connecting.clear()

    def _on_dial_voice_complete(self, name, result, error, percents):
        if (not self.ongoing_call.isSet()) and (error is None):
            self.ongoing_call.set()

    def _on_answer_call_complete(self, name, result, error, percents):
        if (self.ongoing_call.isSet()) and (error is not None):
            self.ongoing_call.clear()

    def _on_incoming_call(self, state_machine, event_type, data):
        self._log.debug("<- [event_type={}] [data={}]".format(event_type, data))

        if (data["Status"] == "IncomingCall") and (not self.ongoing_call.isSet()):
            self.ongoing_call.set()
            if IncomingCallEvent in self._user_callbacks.keys():
                self._user_callbacks[IncomingCallEvent](IncomingCallEvent(data["Number"]))

        elif ((data["Status"] == "CallEnd") or (data["Status"] == "CallLocalEnd")) and self.ongoing_call.isSet():
            self.ongoing_call.clear()
            if EndCallEvent in self._user_callbacks.keys():
                self._user_callbacks[EndCallEvent](EndCallEvent(data["Number"]))

    def _on_incoming_sms(self, state_machine, event_type, data):
        self._log.debug("<- [event_type={}] [data={}]".format(event_type, data))

    def _on_incoming_ussd(self, state_machine, event_type, data):
        self._log.debug("<- [event_type={}] [data={}]".format(event_type, data))
