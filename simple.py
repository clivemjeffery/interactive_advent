from datetime import datetime
from mote import Mote
import time

mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

while True:
	mote.clear()
	mote.set_pixel(1, 0, 200, 0, 0)
	mote.show()
	time.sleep(2)
	mote.set_pixel(1, 0, 0, 200, 0)
	mote.set_pixel(1, 1, 0, 0, 200)
	mote.show()
	time.sleep(2)
