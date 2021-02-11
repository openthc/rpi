# In-Store Menu via RPi

## Slideshow

Add files to `$HOME/Pictures` then run `./slideshow.sh`


## Dynamic Menu

Edit HTML Files directly, using some provided examples.
Remeber to include the JavaScript to auto-advance, rotate, etc.

```
<script src="menu.js"></script>
```

## Alternatives

* https://info-beamer.com/hosted#pricing

### Hardware Notes

You may need to adjust `/boot/config.txt` on the Pi for screen size.

```
framebuffer_width=1920
framebuffer_height=1080
```

On **Samsung** TVs it also helps to rename the input to "PC"
