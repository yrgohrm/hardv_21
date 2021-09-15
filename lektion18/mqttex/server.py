import paho.mqtt.client as mqtt
import struct

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("some/topic", qos=1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # if we subscribe to more than one topic we need
    # to check which topic sent this message
    if msg.topic == "some/topic":
        # By using unpack with the same format as we used for pack
        # we will get a tuple back with our data
        (id, rnd) = struct.unpack("!Qb", msg.payload)
        print(f"random: {id:#0x} {rnd}")

def byebye(client, userdata, rc):
    print("Error error!")
    exit(-1)

# Create a MQTT client with callbacks for
# connecting to the MQTT server and receiving data
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = byebye

client.connect("localhost", port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()
