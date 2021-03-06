import threading
import time
from tkinter.constants import *

from pyphone import controllers
from pyphone.controllers.controller import Controller


class InfoController(Controller):
    def __init__(self, panel):
        super().__init__(panel)

        self._update_thread = threading.Thread(target=self._update_worker, daemon=True)
        self._update_thread.start()

    def cleanup(self):
        super().cleanup()
        self._update_thread.join()

    def _update_worker(self):
        from pyphone.controllers import GammuController

        while not self.stopped.isSet():
            if self.panel_visible and controllers.get(GammuController).connected.isSet():
                self._get_system_info()
                self._get_connection_info()
                self._get_battery_status()
            time.sleep(5)

    def _get_system_info(self):
        from pyphone.controllers import GammuController

        system_info = []
        system_info_commands = [
            "GetManufacturer",
            "GetModel",
            "GetFirmware",
            "GetNetworkInfo",
            "GetSecurityStatus",
            "GetDisplayStatus",
            "GetSMSStatus",
            "GetCalendarStatus",
            "GetFileSystemStatus",
            "GetIMEI",
            "GetOriginalIMEI",
            "GetSIMIMSI",
            "GetPPM"
        ]

        def add_system_info(name, result, error, percents):
            system_info.append((name, result if error is None else error))

        for command in system_info_commands:
            controllers.get(GammuController).enqueue_command(command, callback=add_system_info)

        while len(system_info) < len(system_info_commands):
            if self.stopped.wait(0.1):
                return

        for entry in self.panel.system_info_tree.get_children():
            self.panel.system_info_tree.delete(entry)

        for entry in system_info:
            key = entry[0]
            value = entry[1] if entry[1] is not None else ""
            self.panel.system_info_tree.insert("", END, text=key, values=(value,))

    def _get_connection_info(self):
        from pyphone.controllers import GammuController

        def set_connection_info(name, result, error, percents):
            if not self.stopped.isSet():
                signal_percent = int(result["SignalPercent"]) if error is None else 0
                signal_strength = int(result["SignalStrength"]) if error is None else 0
                self.panel.signal_status_bar.configure(value=signal_percent)
                self.panel.signal_status_text.configure(text="{} dBm".format(signal_strength))

        controllers.get(GammuController).enqueue_command("GetSignalQuality", callback=set_connection_info)

        return

    def _get_battery_status(self):
        from pyphone.controllers import GammuController

        def set_battery_status(name, result, error, percents):
            if not self.stopped.isSet():
                battery_percent = int(result["BatteryPercent"]) if error is None else 0
                self.panel.battery_status_bar.configure(value=battery_percent)
                self.panel.battery_status_text.configure(text="{} %".format(battery_percent))

        controllers.get(GammuController).enqueue_command("GetBatteryCharge", callback=set_battery_status)
