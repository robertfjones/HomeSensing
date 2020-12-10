#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient


import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/home/pi/mqtt/log/mqtt.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Mqtt to MongoDb App Running.')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if rc == 0:
        logging.info("Connected with result code: "+str(rc))
        client.subscribe("Home/#")
    else:
        logging.error("Connected with error code: "+str(rc))

def on_message(client, userdata, msg):
    receiveTime=datetime.datetime.now()
    message=msg.payload.decode("utf-8")
    isfloatValue=False
    try:
        # Convert the string to a float so that it is stored as a number and not a string in the database
        val = float(message)
        isfloatValue=True
    except:
        isfloatValue=False

    if isfloatValue:
        print(str(receiveTime) + ": " + msg.topic + " " + str(val))
        post={"time":receiveTime,"topic":msg.topic,"value":val}
    else:
        print(str(receiveTime) + ": " + msg.topic + " " + message)
        post={"time":receiveTime,"topic":msg.topic,"value":message}
    
    try:
        msg_id = collection.insert(post)
        print(msg_id)
    except:
        logging.error("Message insert failed: {}".format(post))


# Set up client for MongoDB
mongoClient=MongoClient('mongodb://pythonUser:autom8@localhost:27017/')
try:
    client_info = mongoClient.server_info()
    logging.info("MongoDB Connected: {}".format(client_info))
except:
    logging.error("MongoDB Connection Error")
try:
    db=mongoClient.local
    logging.info("MongoDB User Connected: {}".format(db))
except:
    logging.info("MongoDB User Connected: {}".format(db))
collection=db.sensors

# Initialize the client that should connect to the Mosquitto broker
try:
    client = mqtt.Client()
    logging.info("MQTT Start Client")
except:
    logging.error("MQTT Client Error")

client.on_connect = on_connect
client.on_message = on_message

try:
    c = client.connect("192.168.1.39", 1883, 60)
    logging.info("MQQT Client Connect Sucess: " + str(c))
except:
    logging.error("MQTT Client Connect Error: " + str(c))

try:
    client.subscribe("Home/#")
except:
    logging.error("Client subscription error")

# Blocking loop to the Mosquitto broker
client.loop_forever()