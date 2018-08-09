#!/usr/bin/env python3
#
# Read Serial using Serial module
#

import serial


#
# Connect
ser = serial.Serial('/dev/ttyUSB0', 2400, bytesize=7, parity=serial.PARITY_NONE, stopbits=1, xonxoff=0, rtscts=0)

line_idx = 0
line_tmp = ""

while True:

	line = ser.readline().strip()
	line_idx = line_idx + 1


	# print line.encode("hex")
	#if 10 == line_idx:
	if line != line_tmp:
		print(">>>{0}[[[").format(line)
		line_tmp = line
		#/if
	#	line_idx = 0
	# /if

# /while
