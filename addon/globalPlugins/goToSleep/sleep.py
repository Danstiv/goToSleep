import ctypes


def goToSleepS3():
    ctypes.windll.powrprof.SetSuspendState(False, False, False)


def goToSleepS0():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)
