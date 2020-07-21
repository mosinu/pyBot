# Python script to hide when I am idle and learn pyautogui
import pyautogui as pag
import time
import threading
from time import sleep
from random import randint

x = 50   #how many times to run
startx = 703
starty = 731

#print current position
print(pag.position())
while True:
	pag.click(startx, starty,2)
	pag.typewrite(".")
	pag.typewrite(["enter"])
	pag.typewrite(".")
	pag.typewrite(["enter"])
	print(pag.position())
	sleep(60)
	pag.moveTo(startx, starty,duration=.5)
	pag.typewrite(".")
	pag.typewrite(["enter"])
	print(pag.position())
	sleep(60)
	pag.moveTo(startx, starty,duration=.5)
	pag.typewrite(".")
	pag.typewrite(["enter"])
	print(pag.position())
	pag.click(startx, starty,2)
	pag.typewrite(".")
	pag.typewrite(["enter"])

	startx = startx + 1
	starty = starty + 1

	x = x - 1
	if x == 0:
		break