# DHT22

Connecting a [DHT22](https://amzn.to/2KEA9Jh) sensor to our EMC-RPi.
It's just like the DHT11 but has better precision.

## Wiring

    DHT22 <=> Pi-GPIO
        1 <=> 3V3-Rail
        2 <=> PIN#11
        3 <=> NC
        4 <=> GND

You don't need to wire in a resistor because the Pi has them [built in](https://raspberrypi.stackexchange.com/questions/12161/do-i-have-to-connect-a-resistor-to-my-dht22-humidity-sensor).


## Dependencies

	git clone https://github.com/adafruit/Adafruit_Python_DHT.git
	cd Adafruit_Python_DHT
	sudo python3 setup.py install
