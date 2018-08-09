# DHT11

Connecting a [DHT11](https://amzn.to/2MvuqY5) sensor to our EMC-RPi.

## Wiring

    DHT11 <=> Pi-GPIO
        1 <=> 3V3-Rail
        2 <=> PIN#11
        3 <=> NC
        4 <=> GND

You don't need to wire in a resistor because the Pi has them [built in](https://raspberrypi.stackexchange.com/questions/12161/do-i-have-to-connect-a-resistor-to-my-dht22-humidity-sensor).


## Dependencies

	git clone https://github.com/adafruit/Adafruit_Python_DHT.git
	cd Adafruit_Python_DHT
	sudo python3 setup.py install


## See Also

 * https://github.com/netikras/r-pi_DHT11.git
 * https://github.com/szazo/DHT11_Python.git
 * https://www.google.com/search?q=dht11+fractional+temperature&oq=dht11+fractional+temperature&aqs=chrome..69i57.5428j0j7&sourceid=chrome&ie=UTF-8
 * https://mcuoneclipse.com/2015/03/27/using-the-dht11-temperaturehumidity-sensor-with-a-frdm-board/
 * http://www.instructables.com/id/Build-Your-First-IOT-with-a-Raspberry-Pi-DHT11-sen/
 * http://docs.gadgetkeeper.com/pages/viewpage.action?pageId=7700673 
 * https://medium.com/dyi-electronics/raspberry-pi-and-dht11-humidity-sensor-cccf6b3072ad
 * http://www.uugear.com/portfolio/dht11-humidity-temperature-sensor-module/
 * http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
 * http://www.instructables.com/id/Raspberry-Pi-Temperature-Humidity-Network-Monitor/
 * http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
 * https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview
 * https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=47391
 * https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=47771
 * http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
