import RPi.GPIO as GPIO
from time import sleep
from os import system

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)     #A
GPIO.setup(17,GPIO.OUT)   #B
GPIO.setup(27,GPIO.OUT)   #C
GPIO.setup(22,GPIO.OUT)   #D
GPIO.setup(5,GPIO.OUT)     #E
GPIO.setup(6,GPIO.OUT)     #F
GPIO.setup(13,GPIO.OUT)   #G
#Pin Selector
GPIO.setup(21,GPIO.OUT)	#Ten's Selector Pin
GPIO.setup(20,GPIO.OUT)	#Unit's Selector Pin

Num = [[True,True,True,True,True,True,False],[False,True,True,False,False,False,False],[True,True,False,True,True,False,True],[True,True,True,True,False,False,True],[False,True,True,False,False,True,True],[True,False,True,True,False,True,True],[True,False,True,True,True,True,True],[True,True,True,False,False,False,False],[True,True,True,True,True,True,True],[True,True,True,True,False,True,True]]

sequence = [4,17,27,22,5,6,13]

def lightUp(number,sleepFlag):
	for i in range(7):
		if number[i] == True:
			GPIO.output(sequence[i],GPIO.LOW)
	if(sleepFlag == 1):
		sleep(.5)
		system('python LEDoff.py')
tens = 0
while(True):
	GPIO.output(21,GPIO.HIGH)
	GPIO.output(20,GPIO.LOW)
	lightUp(Num[tens],1)
	tens += 1
	if tens == 10:
		tens = 0
	GPIO.output(21,GPIO.LOW)
	GPIO.output(20,GPIO.HIGH)
	lightUp(Num[0],1)
	for i in range(1,10):
		lightUp(Num[i],1)
	
