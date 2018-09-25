# Drive an RGB LED

## Pinout

 Red     <=> 11
 Cathode <=> _
 Green   <=> 13
 Blue    <=> 15


## Control

```
./rgb.py <color> <on-duration> <fade-in> <fade-out>
./rgb.py #336699 
./rgb.py #556677 fade
./rgb.py off
./rgb.py #ffffff fade 500
./rgb.py off fade 500
```


### See Also

 * https://www.instructables.com/id/Raspberry-Pi-3-RGB-LED-With-Using-PWM/
 * https://www.pidramble.com/wiki/hardware/rgb-led-gpio
