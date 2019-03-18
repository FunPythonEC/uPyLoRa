
import network
from robust import MQTTClient
import machine as m
import time
from lora import LoRa

def cb(msg):
    temp, humid = msg.split('|')
    msg = b'{"temp":%s, "humid":%s}' % (temp, humid)
    print(msg)
    client.publish(b"/v1.6/devices/esp32lora", msg)

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan() # Scan for available access points
sta_if.connect("SSID", "PASS") # Connect to an AP
sta_if.isconnected()
time.sleep(5)

ubidotsToken = "ubiotstoken"
clientID = "clientid"

client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken)
client.connect()

lora=LoRa()
lora.set_callback()
lora.wait_msg()

