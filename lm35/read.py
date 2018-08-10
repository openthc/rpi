#!/usr/bin/env python3
#
# Read the LM35 Sensor
#

import getopt
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
MCP_CHANNEL = 1

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

X = mcp.read_adc(MCP_CHANNEL)
X = float(X)

V1 = X * 3.3 / 1024.0
#V2 = X * (3300 / 1024)

#Vm = V * 1000

C1 = "C1"
C2 = "C2"
# C1 = ((Vm - 100.0) / 10.0) - 40.0
# C2 = (X * 3300 / 1024) - 50

print("X:{}, V1:{}, V2:{}, C1:{}, C2:{}".format(X, V1, V2, C1, C2))
