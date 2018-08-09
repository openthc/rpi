#!/usr/bin/env python3
"""
Read the DHT11, output to STDOUT
"""

# Import all the libraries we need to run
import sys
import RPi.GPIO as GPIO
import Adafruit_DHT

# The physical pin
pin = 11
if (len(sys.argv) >= 2):
	pin = int(sys.argv[1])


# Setup the pins we are connect to
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#H, C = Adafruit_DHT.read(Adafruit_DHT.DHT11, pin)
H, C = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)


#
# Output

F = (C * 9 / 5) + 32

print("Temperature: %0.1f C" % C)
print("Temperature: %0.1f F" % F)
print("Humidity:    %0.1f%%" % H)
