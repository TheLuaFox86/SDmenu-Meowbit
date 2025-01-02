from meowbit import screen
import os
from time import sleep_ms
os.chdir("pics")
pl = os.listdir()
screen.sync = 0
while 1:
	try:
		for p in pl:
			screen.fill(0)
			screen.loadBmp(p, -1, -1)
			screen.refresh()
			time.sleep_ms(5000)
	
	except:
		screen.fill(0)
		screen.text("Error")
		screen.refresh()
