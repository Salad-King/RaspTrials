import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3)<<8)+adc[2]
	return data

def ConvertTemp(data,places):
	temp = ((data * 330)/float(1023))
	temp = round(temp,places)
	return temp

delay = .2
tempChannel = 0

while True:
	tempLevel = ReadChannel(tempChannel)
	temp = ConvertTemp(tempLevel,2)
	time.sleep(delay)
	
	print("Temp : {}  {} deg C".format(tempLevel,temp))
