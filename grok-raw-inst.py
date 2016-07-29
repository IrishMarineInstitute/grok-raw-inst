import pygrok
import os.path
import paho.mqtt.client as paho

#
# This bit needs parameterising
#
mqtt_server  =  'mqtt.marine.ie'
mqtt_port  =  1883
#mqtt_channel  =  'spiddal-ctd'
#grok_pattern = '%{MI_PREFIX}%{SPACE}%{IDRONAUT_OCEAN7_304}'
mqtt_channel  =  'spiddal-fluorometer'
grok_pattern = '%{MI_PREFIX}%{WETLABS_ECO_FLNTU_3137}'




msgCount = 0
#
# Import custom patterns for Grok
#
pats_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'patterns')

def on_connect(client, userdata, flags, rc):
    global mqtt_channel
    client.subscribe(mqtt_channel)
def on_message(client, userdata, msg):
    global grok_pattern
    print pygrok.grok_match(msg.payload, grok_pattern, custom_patterns_dir = pats_dir)
    global msgCount
    msgCount = msgCount + 1
    if msgCount > 10:
        client.disconnect()

client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_server, mqtt_port, 60)
client.loop_forever()
