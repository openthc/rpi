# Printer Connection

These tools allow for web-applications, or local-network applications to print to whatever is connected to this.

 * Label Printers
 * Receipt Printers


## CUPS

This device simply uses CUPS, configured to allow for remote configuration and printing.
Any printers added to this device should have sharing enabled so they are visible to tablets and other systems.

```bash
sudo apt-get install cups cups-filters cups-filters-core-drivers printer-driver-dymo
sudo apt-get install libcupsppdc1-dev libfontembed-dev libcupsmime1-dev libcupsimage2-dev libcupsfilters-dev libcups2-dev
update-rc.d cups-browsed remove
```

We have also provided a sample cupsd.conf file

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


## Zebra

Works out of the box, just configure the default values correctly


## Polling Service

Some times you have an external application that needs to print directly.
For example, some internal web-tools, or other connected devices that may not be that intelligent.
The polling service runs to query an endpoint which can provide a document to print.

```bash
export OPENTHC_PRINT_URI="https://example.com/api/v2018/print/poll"
export OPENTHC_PRINT_KEY="$HASH"
export OPENTHC_PRINT_NAP="4"
/usr/bin/nohup ./poll.py >poll.log 2>&1 &
```


## Print Server

Setup Apache and Add SSL, then link in the print-server.php script
It's a good idea here to give these systems a static IP address on your network.

    apt install php apache2
    a2enmod ssl
    a2ensite default-ssl
    cd /var/www/html
    ln -s $REPO/printer/print-server.php

Once that is configured, then devices that want to print simply need to know about this EMC device as a print server and send the proper request.


### SSL

    openssl req -x509 -newkey rsa:4096 \
        -subj '/C=US/ST=Washington/L=Seattle/O=OpenTHC/OU=Printer/CN=localhost' \
        -keyout emc-device.key -out emc-device.crt -days 3650

