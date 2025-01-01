#config
background = (0, 0, 255)
wdir = "MeowbitSD"
debugmode = 0
#code
from meowbit import *
screen.sync = 0
import os
import math
from time import sleep_ms
screen.fill(0)
screen.loadBmp("logo.bmp", -1, -1)
screen.text("SDmenu", 0, 0, 2, 255)
screen.text("By TheLuaFox86", 0, 120)
screen.refresh()
buzzer.melody("c6:1 f6:2", 120)
time.sleep_ms(1000)


if wdir == "":
	print("operating in root")
else:
	os.chdir(wdir)
	print("operating in " + wdir)


dl = os.listdir()
selected = 0
count = 0
pg = 1
def option(txt, y):
	if selected == count:
		screen.text(txt, 0, y,  1, 80)
		return 1
	else:
		screen.text(txt, 0, y)
		return 0
go = 1
while go:
	if selected > len(dl) :
		selected = 0
	
	if selected < 0:
		selected = len(dl)
		
	pg = math.floor(selected / 4) + 1
	calc = pg * 4
	if debugmode:
		screen.text(selected, 0, 8)
		screen.refresh()
	
	try:
		screen.fill(background)
		screen.text("SDmenu", 0, 0)
		count = 0
		y = 20
		if sensor.btnValue("down"):
			selected = selected + 1
	
		if sensor.btnValue("up"):
			selected = selected - 1
			
		if sensor.btnValue("b"):
			os.chdir("..")
			dl = os.listdir()
			
		if selected <= -1:
			selected = 0
	
		if option("...", y):
			if sensor.btnValue("a"):
				os.chdir("..")
				dl = os.listdir()
	
		screen.text("(/\),(\/) to scroll", 0, 81)
		screen.text("(A) folder (B) Back", 0, 89)
		screen.text("(<) boot (>)run py", 0, 97)
		for d in dl:
			count =  count + 1
			if count <= calc:
				if count >= calc - 4:
					y = y + 11
					if option(d, y):
						if sensor.btnValue("a"):
							os.chdir(d)
							dl = os.listdir()
					
						if sensor.btnValue("left"):
							try:
								go = 0
								screen.fill(0)
								screen.sync = 1
								os.chdir(d)
								execfile("main.py")
							except:
								screen.sync = 0
								go = 1
								screen.fill(0)
								screen.text("fail")
								screen.refresh()
								buzzer.melody("a3:2 r a3:2", 120)
			
			
						if sensor.btnValue("right"):
							try:
								go = 0
								screen.fill(0)
								screen.sync = 1
								execfile(d)
							except:
								screen.sync = 0
								go = 1
								screen.fill(0)
								screen.text("fail")
								screen.refresh()
								buzzer.melody("a3:2 r a3:2", 120)
			
			
				
		screen.refresh()
	except:
		os.chdir("..")
		dl = os.listdir()
