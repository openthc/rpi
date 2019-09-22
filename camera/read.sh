#!/bin/bash

set -o errexit
set -o nounset

dt=$(date +%Y%m%dT%H%M%S)
raspistill \
	--nopreview \
	--verbose \
	--output "image-$dt.jpeg"
