import paho.mqtt.publish as publish
import time
import random
#import Adafruit_DHT
#from datetime import datetime, date, time, timedelta
#import calendar
#import RPi.GPIO as GPIO, time,os
# import spidev
#from gpiozero import MCP3008

#spi=spidev.SpiDev()
#spi.open(0,0)

INFLUXDB_ADDRESS = '127.0.0.1'
MQTT_ADDRESS = '127.0.0.1'

class Sensor(object):

    def __init__(self, name="SensorGeneric"):
        self.name = name

    def read_data(self):
        return None

    def read_spi_channel(self, channel):
        #       spidata=spi.xfer2([1,(8+channel)>>4,0])
        #data = (((spidata[1] %3 )<< 8 )+ spidata[2])
        #return data
        return None
    def __str__(self):
        return "__"+self.name+"__"+":{}".format(self.read_data())


class Temperatura(Sensor):

    def __init__(self, name):
        Sensor.__init__(self, name)

    def read_data(self):
        #humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)temperature = 43   	
	temperature = random.randint(0, 43)
	publish.single("sensor", temperature, hostname = MQTT_ADDRESS)
	print("__"+self.name+"__" + "published to MQTT ADDRESS: " + MQTT_ADDRESS)
        return temperature

class Humidity(Sensor):

    def __init__(self, name):
        Sensor.__init__(self, name)

    def read_data(self):
        #humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
        humidity = random.randint(0,100)
	#print(self.name+":"+self.read_data())
	publish.single("sensor", humidity, hostname= MQTT_ADDRESS)
	print("__"+self.name+"__" + "published to MQTT ADDRESS: " + MQTT_ADDRESS)
        return humidity

if __name__ == "__main__":
    while True:
        tm = Temperatura("Temperatura")
	print (tm)
        hm = Humidity ("Humitat")
        print (hm)
        time.sleep(5)
