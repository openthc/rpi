## DHT11-Python

 * https://github.com/szazo/DHT11_Python.git

```
diff --git a/dht11_example.py b/dht11_example.py
index 8dfa3ff..d99e3ea 100644
--- a/dht11_example.py
+++ b/dht11_example.py
@@ -5,11 +5,11 @@ import datetime
 
 # initialize GPIO
 GPIO.setwarnings(False)
-GPIO.setmode(GPIO.BCM)
+GPIO.setmode(GPIO.BOARD)
 GPIO.cleanup()
 
 # read data using pin 14
-instance = dht11.DHT11(pin=14)
+instance = dht11.DHT11(pin=7)
 
 while True:
     result = instance.read()
@@ -17,5 +17,7 @@ while True:
         print("Last valid input: " + str(datetime.datetime.now()))
         print("Temperature: %d C" % result.temperature)
         print("Humidity: %d %%" % result.humidity)
+    else:
+       print("Not Valid")
 
     time.sleep(1)

```

 * https://github.com/netikras/r-pi_DHT11.git

## See Also

https://www.google.com/search?q=dht11+fractional+temperature&oq=dht11+fractional+temperature&aqs=chrome..69i57.5428j0j7&sourceid=chrome&ie=UTF-8

https://mcuoneclipse.com/2015/03/27/using-the-dht11-temperaturehumidity-sensor-with-a-frdm-board/

http://www.instructables.com/id/Build-Your-First-IOT-with-a-Raspberry-Pi-DHT11-sen/

http://docs.gadgetkeeper.com/pages/viewpage.action?pageId=7700673 

https://medium.com/dyi-electronics/raspberry-pi-and-dht11-humidity-sensor-cccf6b3072ad

http://www.uugear.com/portfolio/dht11-humidity-temperature-sensor-module/

http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

http://www.instructables.com/id/Raspberry-Pi-Temperature-Humidity-Network-Monitor/

http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=47391

https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=47771

http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

