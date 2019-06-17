import time
import threading
from neopixel import *
import random
import math


# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


class LedCircle():


	def __init__(self):
		self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
		self.strip.begin()
		self.thread = threading.Thread(target=self.draw)
		self.running = True
		self.thread.start()
		self.animation = "rainbow"
		self.duration = 3
		self.color = (52, 152, 219)

	def wheel(self, pos):
		"""Generate rainbow colors across 0-255 positions."""
		if pos < 85:
			return Color(pos * 3, 255 - pos * 3, 0)
		elif pos < 170:
			pos -= 85
			return Color(255 - pos * 3, 0, pos * 3)
		else:
			pos -= 170
			return Color(0, pos * 3, 255 - pos * 3)



	def draw(self):
		i=0
		wait_s = 0.05
		percentage = 0
		temps = 0
		while self.running:
			for i in range(0, self.strip.numPixels()):
				#self.strip.setPixelColor(i, Color(int(random.random() * 255),int(random.random() * 255), int(random.random() * 255)))
				if (self.animation == "rainbow"):
					j = int(percentage * 255)
					self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
				elif (self.animation == "fade"):
					ratio = math.pow(math.sin(percentage*math.pi),2)
					r = int( ratio * self.color[0])
					g = int( ratio * self.color[1])
					b = int( ratio * self.color[2])
					self.strip.setPixelColor(i, Color(r,g,b))
			temps = ((temps + wait_s) % self.duration)
			percentage = temps / self.duration
			self.strip.show()
			time.sleep(wait_s)

	def stop(self):
		self.running = False
		i=0
		for i in range(0, self.strip.numPixels()):
			self.strip.setPixelColor(i, Color(0,0,0))
		self.strip.show()

if __name__ == '__main__':
	test = LedCircle()
	time.sleep(10)
	test.stop()
	print("testsfrsdfsdf")
