#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
while 1:
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
      	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
	time.sleep(1)
