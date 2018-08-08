#
# Find /dev/ttyUSB* or /dev/* for Serial
#  Then open each port, using known scale defaults
#  Then test to see what settings actually produce reasonable bytes
#    Reasonable Bytes means one of the three or four standard scale output types
#

import glob
#import serial

port_list = glob.glob("/dev/ttyUSB*")

# 2400, 7, Even, CRLF
baud_list = [ 2400, 9600, 19200 ]
byte_size_list = [ 7, 8 ]
#parity_list = [ serial.PARITY_NONE ]
#stop_bit_list = [ 0, 1 ]


for port in port_list:

	print port

	for baud in baud_list:
		print "serial.Serial('{0}', {1}\n".format(port, baud)
		# ser = serial.Serial('/dev/ttyUSB0', baud, bytesize=7, parity=serial.PARITY_NONE, stopbits=1, xonxoff=0, rtscts=0)
	#/for

#/for


# 
