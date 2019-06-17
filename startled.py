import LedCircle
import time

ledCircle = LedCircle.LedCircle()
ledCircle.start()
ledCircle.animation = "fade"
ledCircle.duration = 0.5
time.sleep(0.5)
ledCircle.duration = 0.5
time.sleep(0.5)
ledCircle.stop()
