import datetime
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import main as pr

MQTT_ADDRESS = '127.0.0.1'
MQTT_TOPIC = 'sensor'

INFLUXDB_DATABASE = "sensor"


idb = InfluxDBClient(database= INFLUXDB_DATABASE)

gr = [{
    "measurement": "",
    "time": 0,
    "fields":
        {
            "value": 0
        }
}, {
    "measurement": "",
    "time": 0,
    "fields":
        {
            "value": 0
        }
}, {
    "measurement": "",
    "time": 0,
    "fields":
        {
            "value": 0
        }
}, {
    "measurement": "",
    "time": 0,
    "fields":
        {
            "value": 0
        }
}, {
    "measurement": "",
    "time": 0,
    "fields":
        {
            "value": 0
        }
}, {
    "measurement": "",
    "time": 0,
    "fields":
        {
            "value": 0
        }
}, ]

sensor_tm = str(pr.Temperatura("Temperatura"))
a, temperatura = sensor_tm.split(":")
print("Hola" + temperatura)

sensor_hm = str(pr.Humidity("Humitat"))
a, humitat = sensor_hm.split(":")
print("Hola" + humitat)

def on_connect(client, userdata, flags, rc):
	print ("Connected: " + str(rc) + client.subscribe("sensor"))
	client.subscribe("sensor")


def missatge(client, userdata, msg):
    	global sensor
	print "Hola, he rebut un missatge"
	sensor = str(msg.payload)
	print "rebut: ", sensor
	mesurement = ["temperatura", "humitat", "ldr", "vent", "pluja"]

	jsondata[0]["time"] = datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
	jsondata[0]["measurement"] = "temperatura"
	jsondata[0]["fields"]["value"] = temperatura

	jsondata[1]["time"] = datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
	jsondata[1]["measurement"] = "humitat"
	jsondata[1]["fields"]["value"] = humitat

	print jsondata
	idb.write_points(jsondata)


client = mqtt.Client()
print("Setting the mqtt client")
client.on_connect = on_connect
print("Conneting to " + MQTT_ADDRESS)
client.on_message = missatge

client.connect(MQTT_ADDRESS, 1883, 60)

while True:
	client.loop()
