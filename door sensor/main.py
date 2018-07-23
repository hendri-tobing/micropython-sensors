from machine import Pin
from time import sleep
from configfile import pindoor

door = Pin(pindoor, Pin.IN, Pin.PULL_UP)

def doorVal():
    try:
        status = door.value()
        return status
    except Exception as e:
        return 0

stateDoor = 0

while True:
    status = doorVal()

    if status != stateDoor:
        if status = 1:
            print("door open")
        if status = 0:
            print("door closed")
        else:
            print("something is wrong")
        stateDoor = status
    else:
        pass