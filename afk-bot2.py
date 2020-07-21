# Python script to keep me from being idle and learn pyautogui
import pyautogui as pag
import time
import threading
from time import sleep
from random import randint
from random import seed

x = 500   #how many times to run
startx = 703 #starting spot for x
starty = 731 #start spot for y

#print current position
print(pag.position())
pag.click(1568, 49) # Click on a window intially
while True:
	pag.moveTo(startx, starty,duration=1)
	print(pag.position())
	sleep(60)
	pag.moveTo(1560, 100,duration=1)
	print(pag.position())
	sleep(60)
	pag.moveTo(startx, starty,duration=1)
	print(pag.position())
	#generate semi-random place to move cursor to
	for _ in range(1):
		place = randint(0,50)
		startx = startx + place
		starty = starty + place

	x = x - 1
	if x == 0:
		break