# hello-python
This is a barebones resin.io project to demonstrate running python code on the Intel Edison.
Currently it builds upon a Debian jessie base image with [systemd][systemd-link] init system enabled. It has the latest [libmraa][mraa-link] baked into it, so you can use it from python my doing an `import mraa` as see in `app/hello.py`

This basic python example just prints a message to console and blinks/toggles the GPIO 13. If your Edison is on the arduino base board, you should see the onboard LED blinking, if you are any of the other base board, you will need to connect up an external LED and resistor to GPIO 13.

For an explination on how [resin.io](https://resin.io/) uses Dockerfiles check out the [Dockerfile guide](http://docs.resin.io/#/pages/dockerfile.md)
 . Additionally if you want to learn how to optimise your Dockerfile look over [here](http://docs.resin.io/#/pages/build-optimisation.md)


[mraa-link]:https://github.com/intel-iot-devkit/mraa
[systemd-link]:https://wiki.archlinux.org/index.php/Systemd
