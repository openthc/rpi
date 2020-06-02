#!/usr/bin/env python3
#
# Read Serial using Serial module
#

import sys
import serial
from urllib.parse import urlencode
from urllib.request import Request, urlopen


port = "/dev/ttyUSB0"
baud = 9600


#
# Output File Too?
output_file = None
if len(sys.argv) >= 2:
	output_file = sys.argv[1]


#
# Output to WebApplication
output_link = None
if len(sys.argv) >= 3:
	output_link = sys.argv[2]


#
# Connect
ser = serial.Serial(port, baud , bytesize=7, parity=serial.PARITY_NONE, stopbits=1, xonxoff=0, rtscts=1)

line_tmp = ""

while True:

	line = ser.readline().strip()
	# print line.encode("hex")

	if line != line_tmp:

		print(">>>{0}[[[".format(line))
		line_tmp = line

		# Push Data to File
		if (output_file):
			fo = open(output_file, "w")
			fo.write(str(line))
			fo.close()
		#/if

		# Push Data to Web
		if (output_link):
			output_data = {
				'line': line
			}
			req = Request(output_link, urlencode(output_data).encode())
			res = urlopen(req).read()
			# Errors Ignored

		#/if

	# /if

# /while
