import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26,GPIO.IN)

while True:
	data = GPIO.input(26)
	#print(data)
	if(data ==True):
		print("Heat Detected")
	else:
		print("Nothing")
	sleep(1)
