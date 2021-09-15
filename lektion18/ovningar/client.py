import paho.mqtt.client as mqtt

# Create a MQTT client and register a callback for connect events
client = mqtt.Client()

# Connect to a broker
client.connect("broker.hivemq.com", port=1883, keepalive=60)

# Start a background loop that handles all broker communication
client.loop_start()

# Send the message
msg = client.publish("yrgo/ela20/hrm/hello", payload="Hello World eller!?", qos=1)
msg2 = client.publish("yrgo/ela20/hrm/other", payload="Annat meddelande!", qos=1)

# If python exits immediately it does not have the time to send
# the message
msg.wait_for_publish()
msg2.wait_for_publish()

client.disconnect()
