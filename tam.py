import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while(True):
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(22,GPIO.LOW)
#	GPIO.output(17,GPIO.HIGH)
	sleep(0.5)
	GPIO.output(22,GPIO.HIGH)
	GPIO.output(17,GPIO.LOW)
#	GPIO.output(27,GPIO.HIGH)
	sleep(0.5)
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
#	GPIO.output(22,GPIO.HIGH)
	sleep(0.5)
