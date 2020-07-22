# MCP3008 ADC

The [MPC3008](https://amzn.to/2KG4s2h) [x4](https://amzn.to/2KEKzIT) is an eight channel ADC.
It's cost effective and interfaces with [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) on the Raspberry Pi.


## Pin Connections

We connect this to SPI0

 MCP3008 #1-8 <=> CH0-CH7 <=> Sensor
    Dgnd   #9 <=> GND     <=> GND-Rail
      CS  #10 <=> BCM#8   <=> PHY#24
     Din  #11 <=> BCM#10  <=> PHY#19
    Dout  #12 <=> BCM#9   <=> PHY#21
     CLK  #13 <=> BCM#11  <=> PHY#23
    Agnd  #14 <=> GND     <=> GND-Rail
    Vref  #15 <=> 3V3     <=> 3v3 Vcc-Rail
     Vdd  #16 <=> 3V3     <=> 3v3-Vcc-Rail


## Dependencies

 * Install: https://github.com/adafruit/Adafruit_Python_MCP3008

    git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
    cd Adafruit_Python_MCP3008
    sudo python3 setup.py install


## Example Code



## Connecting a Sensor

Connect analog sensor to a pin, like CH0.
Then select the channel, and read the value

    mcp3008-select-channel 0
    mcp3008-read


## See Also

 * http://hertaville.com/interfacing-an-spi-adc-mcp3008-chip-to-the-raspberry-pi-using-c.html
 * https://github.com/adafruit/Adafruit_Python_MCP3008/blob/master/examples/simpletest.py
 * https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
 * https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
 * https://www.instructables.com/id/Wiring-up-a-MCP3008-ADC-to-a-Raspberry-Pi-model-B-/
 * http://hertaville.com/interfacing-an-spi-adc-mcp3008-chip-to-the-raspberry-pi-using-c.html
