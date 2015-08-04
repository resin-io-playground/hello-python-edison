#!/usr/bin/python

import mraa
import time

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

# this print statement will appear in the resin.io dashboard logs.
print("hello Mr. Edison!")
while True:
    x.write(1)
    time.sleep(0.2)
    x.write(0)
    time.sleep(0.2)
