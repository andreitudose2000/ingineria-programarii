import os
import random
import time
from threading import Thread

mqtt = None
chairSensorThread = None
asezat = False

def on_connect():
    global chairSensorThread
    if chairSensorThread is None:
        chairSensorThread = Thread(target=chair_sensor_thread)
        chairSensorThread.daemon = True
        chairSensorThread.start()

def chair_sensor_thread():
    global asezat
    while True:
        time.sleep(1)
        chance = random.randint(1, 100)
        if chance <= 1:
            asezat = not asezat
            mqtt.publish("scaun/user_asezat", asezat)
