# LM35

The [LM35]() is an analog temperature sensor.
It must connect in through the MCP3008 ADC.

## Wiring

 * Pin1 <=> 5V
 * Pin2 <=> MCP3008-CH1
 * Pin3 <=> GND

 * Long Wires: https://www.raspberrypi.org/forums/viewtopic.php?t=137680

https://www.raspberrypi.org/forums/viewtopic.php?t=38206

## Reading

    ./read.py

## Data Sheets

 * http://www.ti.com/lit/ds/symlink/lm35.pdf
 * http://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf

## See Also

 * https://learn.adafruit.com/send-raspberry-pi-data-to-cosm/connecting-the-cobbler-slash-mcp3008-slash-tmp36
 * https://learn.adafruit.com/send-raspberry-pi-data-to-cosm/python-script
 * https://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/
