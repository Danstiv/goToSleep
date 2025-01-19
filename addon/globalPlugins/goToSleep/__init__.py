import ctypes

import addonHandler
import globalPluginHandler
from scriptHandler import script

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = 'Go To Sleep'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @script(
        description=_('Go to sleep (S3)'),
        gesture='kb:shift+control+alt+s'
    )
    def script_go_to_sleep_s3(self, gesture):
        ctypes.windll.powrprof.SetSuspendState(False, False, False)
