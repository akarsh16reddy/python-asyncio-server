import os
import signal
import time


def func(signum: int, frame):
    print(f"You raised a SigINT! Signal handler called with {signum}")


_ = signal.signal(signal.SIGINT, func)
while True:
    print(f"Running... {os.getpid()}")
    time.sleep(2)
    # signal.raise_signal(signal.SIGINT)
