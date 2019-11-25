#!/usr/bin/env python3
#
# uses https://github.com/boppreh/keyboard
# pip install keyboard
#
#


import paho.mqtt.client as mqtt
import keyboard

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
print("CONNECTED TO LOCAL MQTT BROKER");
print("PRESS BUTTONS TO SEND MESSAGES, PRESS Z TO END")

def kbCallback(a):
	print(a.name)
	client.publish("GO/CLICKS",a.name);
keyboard.on_press(kbCallback)
keyboard.wait('z');

# client.publish("GO/CLICKS", "A7");
print('QUITTING');
client.disconnect();