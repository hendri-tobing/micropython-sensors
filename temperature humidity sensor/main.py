from dht import DHT22
from machine import Pin
from time import sleep

d = DHT22(Pin(pindht))

while True:
    d = measure()
    tem = d.temperature()
    hum = d.humidity()
    print('Temperature: ', tem, 'Celsius')
    print('Humidity:', hum, '%')
    sleep(10)