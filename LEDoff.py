import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)  #A
GPIO.setup(17,GPIO.OUT) #B
GPIO.setup(27,GPIO.OUT) #C
GPIO.setup(22,GPIO.OUT) #D
GPIO.setup(5,GPIO.OUT)  #E
GPIO.setup(6,GPIO.OUT)  #F
GPIO.setup(13,GPIO.OUT) #G

GPIO.output(4,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(6,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)

