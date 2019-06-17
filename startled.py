import LedCircle
import time

ledCircle = LedCircle.LedCircle()
ledCircle.start()
ledCircle.animation = "fade"
ledCircle.duration = 1
time.sleep(1)
ledCircle.stop()
