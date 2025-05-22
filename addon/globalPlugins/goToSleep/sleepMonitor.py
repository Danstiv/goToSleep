import threading
import time

import queueHandler

from . import sleep


class SleepMonitor(threading.Thread):
    def __init__(self, *, on_start_callback=None, on_stop_callback=None):
        super().__init__()
        self.on_start_callback = on_start_callback
        self.on_stop_callback = on_stop_callback
        self.stop_event = threading.Event()

    def run(self):
        self._call_callback(self.on_start_callback)
        start_time = time.time()
        sleep.goToSleepS0()
        while not self.stop_event.wait(1):
            if time.time() - start_time > 10:
                break
            sleep.goToSleepS0()
        self._call_callback(self.on_stop_callback)

    def stop(self):
        self.stop_event.set()
        self.join()

    def _call_callback(self, callback):
        if callback is None:
            return
        queueHandler.queueFunction(queueHandler.eventQueue, callback)
