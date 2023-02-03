#!/usr/bin/python3
#
# Print Poller and Printer
#
#

"""print-poller

Usage:
  print-poller.py <print-server> <printer-name>
  print-poller.py update-printer-list <print-server>

Options:
  --poll-interval=4  Delay between polling of the print-server

  -h --help          Show this help
  --version          Show version

"""

# import os
import platform
import time

from docopt import docopt
import requests

system_os = platform.system()

if "Windows" == system_os:
	import win32api
	import win32print
# if

if __name__ == '__main__':
	cli_args = docopt(__doc__, version='print-poller v420.23.034')
	print(cli_args)
# /if

#from urllib.parse import urlencode
#//from urllib.request import Request, urlopen

while True:

	res = requests.get(cli_args['<print-server>'])
	if 200 == res.status_code:

		# write file
		out_file = open('PRINT-JOB.pdf', 'wb')
		out_file.write(res.content)

		# print file
		if "Windows" == system_os:
			win32api.ShellExecute(0, "print", out_file, None, ".", 0)
		# else:
			# Ship to CUPS?
		# /if

	elif ((res.status_code >= 300) and (res.status_code <= 399)):
		# Redirects?
		print("Bad Redirect")

	else:
		print("Unknown Status Code")
		print(res.status_code)
	# /if

	time.sleep(8)

# /while
