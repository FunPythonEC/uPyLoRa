from dht import DHT11
from machine import Pin
from time import sleep

from lora import LoRa

dht11 = DHT11(Pin(25))

def readDht():
    dht11.measure()
    return dht11.temperature(), dht11.humidity()

lora = LoRa(header='sasm')

while True:
    temp, humid = readDht()
    lora.send("{0}|{1}".format(temp,humid))
    sleep(5)
    
    
