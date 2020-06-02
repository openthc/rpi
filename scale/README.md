# Scale Integration

Scales with serial outputs can be connected to the Pi via USB-Serial connections.
Then simply read the scale with the provided python script

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
	ST,+00000.00 lb
	ST,+00000.00 lb
	ST,+00000.00 lb
	ST,+00000.00 lb
	ST,+00000.00 lb
	ST,+00000.00 lb
	ST,+00000.00 lb


## Dependencies

 * Python 3
 * [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial_api.html)
 ** Debian: python-serial
 ** Gentoo: dev-python/pyserial

## See Also

* https://github.com/erjiang/usbscale
