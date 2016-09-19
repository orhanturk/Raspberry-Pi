#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
print "yellow Lights on"
GPIO.output(17,GPIO.HIGH)
time.sleep(5)
GPIO.setup(27,GPIO.OUT)
print "red Lights on"
GPIO.output(27,GPIO.HIGH)
time.sleep(5)
GPIO.setup(22,GPIO.OUT)
print "green Lights on"
GPIO.output(22,GPIO.HIGH)
time.sleep(10)
GPIO.cleanup()
