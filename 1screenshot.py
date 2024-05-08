import time
import mss

def screenshot():
    time.sleep(5)
    with mss.mss() as sct:
        sct.shot(output="screenshot.png")

screenshot()