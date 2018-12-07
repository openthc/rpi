# Printer Connection

These tools allow for web-applications, or local-network applications to print to whatever is connected to this.

 * Label Printers
 * Receipt Printers


## CUPS

This device simply uses CUPS, configured to allow for remote configuration and printing.
Any printers added to this device should have sharing enabled so they are visible to tablets and other systems.

```bash
sudo apt-get install cups-filters cups-filters-core-drivers printer-driver-dymo
sudo apt-get install libcupsppdc1-dev libfontembed-dev libcupsmime1-dev libcupsimage2-dev libcupsfilters-dev libcups2-dev
update-rc.d cups-browsed remove
```


## Dymo

These things work right out of the box, no problems


## Star TSC

These devices need to have their CUPS filters and PPD files built from source

Get whatever is the latest drivers from the [Star Micronics Support Page](http://www.starmicronics.com/support/default.aspx?printerCode=CUPS_for_Linux)


```bash
tar -zxf starcupsdrv-3.7.0_linux.tar.gz
cd ./starcupsdrv-3.7.0_linux/SourceCode
tar -zxf starcupsdrv-src-3.7.0.tar.gz
make
sudo ./install/setup
```


# Zebra

Works out of the box, just configure the default values correctly
