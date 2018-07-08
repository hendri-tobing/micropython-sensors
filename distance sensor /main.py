from configfile import *
from hcsr04 import HCSR04
from machine import Pin
from time import sleep_ms

__author__ = 'Hendri L Tobing'

"""
This code is checking distance with sensor hcsr04.
The sensor drive is from https://github.com/rsc1975/micropython-hcsr04

The sensor will check the distance in centimeter, every 1 second (500 ms + 500 ms),
and blinking the LED every 500 ms on pin 
"""

led = Pin(pinled, Pin.OUT, value=1)

def check_distance():
    sensor = HCSR04(trigger_pin=trp, echo_pin=ecp)
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')

while True:
    sleep_ms(500)
    led.value(1)
    distance = check_distance()
    sleep_ms(500)
    led.value(0)

if __name__ == "__main__":
    main()
