import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(27,GPIO.OUT)

while True:
	#sleep(1)
	GPIO.output(27,GPIO.HIGH)
	sleep(0.5)
	GPIO.output(27,GPIO.LOW)
	sleep(0.5)
	#print("IN LOOP")
