# Scale Integration

Scales with serial outputs can be connected to the Pi via USB-Serial connections.
Then simply read the scale with the provided python script.

Simply writes the current value to a file, which can be used by other services.

```shell
./pump.py scale.out
```

Or a more complex setup, feeding a webhook, running as service

```shell
nohup ./pump.py \
  /dev/null \
  'https://app.openthc.dev/api/v2017/scale?_={TOKEN}' \
  >/dev/null 2>&1 &
```


## Publishing

Once captured the data from the scale can be published via any number of methods

 * HTTP
 * SQL
 * WebSocket
 * Redis+Pub/Sub
 * etc


## USB to Serial

- ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
- ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port - Generic or Trendnet TU-S9

## Scale

This service works with nearly any scale that feeds data in via serial connection.
The script configuration may need to be adjusted for the serial port parameters.
Some scales output their data in different formats, this script doesn't care but the next consumer might.


### A&D FX-300i

* Has Scale ID, Supports GLP Reports over Serial
* Defaults: 2400, 7, Even, CRLF
* Works
	
	Standard Line (A&D Standard Format):
	ST,+0013.538  g
	US,+0013.538  g

	Scale ID Lines:- with Scale ID incluced, top-line, and is AlphaNumericSpace [/\w ]
	0000000
	ST,+0013.544  g


## A&D HV-60KC

* Has Scale ID, Supports GLP Reports over Serial
* Update Setting to include the Output over Serial (see manual)
* Default: 2400, 7, Even, CRLF
* Has two ports for Output so settings may need to be on Port 1 or Port 2
* Looking AT the back of the unit, the Left is #2 and the Right is #1
	
	Line Format:
	ST,+00000.00 lb
	ST,+00000.00  g


## Dependencies

 * Python 3
 * [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
 ** Debian: python-serial
 ** Gentoo: dev-python/pyserial

### Windows

On windows you'll need to install **git**.
Get **Python** from the Windows Store.
Install **pyserial** using **pip**.


## See Also

* https://github.com/erjiang/usbscale
