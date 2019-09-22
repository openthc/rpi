# Camera

Enable the camera with `raspi-config`

## Capture

Use the `read.sh` script to generate a file in the current directory named *image-YYYYMMDDThhmmss.jpeg*.

These images could be 2.5MiB each.

## Timelapse

To create a timelapse image add a line like this to your user crontab.
This example captures images every four minutes.

    */4 * * * * cd /path/to/image-storage; /path/to/emc-device/camera/read.sh

Or wrap that in another shell script if more complex capture logic is needed.
Later all these images could be stiched together with `ffmpeg` to make a nice video.

Each image could be 2.5MiB so if you take one picture every four minutes you'll generate 900MiB of data in one day (2.5 * 360).
You'll want to make sure you have enough storage, or reduce the number of images captured.

## See Also

* https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
