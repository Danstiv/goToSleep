import addonHandler
import globalPluginHandler
from scriptHandler import script

from . import sleep

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "Go To Sleep"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @script(description=_("Go to sleep (S3)"))
    def script_go_to_sleep_s3(self, gesture):
        sleep.goToSleepS3()

    @script(description=_("Go to sleep (S0)"))
    def script_go_to_sleep_s0(self, gesture):
        sleep.goToSleepS0()
