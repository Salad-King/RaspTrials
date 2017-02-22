import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.cleanup()
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)  #A
GPIO.setup(17,GPIO.OUT) #B
GPIO.setup(27,GPIO.OUT) #C
GPIO.setup(22,GPIO.OUT) #D
GPIO.setup(5,GPIO.OUT)  #E
GPIO.setup(6,GPIO.OUT)  #F
GPIO.setup(13,GPIO.OUT) #G

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
def lightParts():
	GPIO.output(4,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(6,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
lightParts()
time.sleep(1)
GPIO.output(20,GPIO.HIGH)
time.sleep(1)
GPIO.output(21,GPIO.LOW)

