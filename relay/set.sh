#!/bin/bash
#
# Set the Relay Status
# Get the Relay Status

f=$(readlink -f "$0")
d=$(dirname "$f")

cd "$d"

pin=$(grep "$1" relay.tab | cut -d':' -f2)
if [ -z "$pin" ]
then
	echo "Relay '$1' not found in relay table"
	exit 1
fi


case "$2" in
init)
	gpio -1 mode $pin out
	gpio -1 write $pin 0
	;;
off|0)
	gpio -1 write $pin 0
	;;
on|1)
	gpio -1 write $pin 1
	;;
*)
	gpio -1 read $pin
	;;
esac
