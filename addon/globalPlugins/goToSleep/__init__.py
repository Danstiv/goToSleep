import addonHandler
import globalPluginHandler
import tones
from scriptHandler import script

from . import sleep
from .sleepMonitor import SleepMonitor

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "Go To Sleep"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sleep_monitor = None

    @script(description=_("Go to sleep (S3)"))
    def script_go_to_sleep_s3(self, gesture):
        sleep.goToSleepS3()

    @script(description=_("Go to sleep (S0)"))
    def script_go_to_sleep_s0(self, gesture):
        sleep.goToSleepS0()

    @script(description=_("Go to sleep aggressively (S0)"))
    def script_go_to_sleep_aggressively_s0(self, gesture):
        if self.sleep_monitor is not None:
            self.sleep_monitor.stop()
        self.sleep_monitor = SleepMonitor(
            on_start_callback=self.on_sleep_monitor_start,
            on_stop_callback=self.on_sleep_monitor_stop,
        )
        self.sleep_monitor.start()

    def on_sleep_monitor_start(self):
        self.bindGesture("kb:escape", "cancel_sleep_monitor")

    def on_sleep_monitor_stop(self):
        self.removeGestureBinding("kb:escape")

    def script_cancel_sleep_monitor(self, gesture):
        self.sleep_monitor.stop()
        tones.beep(500, 100)
