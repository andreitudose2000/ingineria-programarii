import random
import time
from datetime import datetime
from threading import Thread

mqtt = None
flask_app = None
asezat = False
chairSensorAsezatThread = None
chairSensorAvertismentThread = None

def on_connect():
    print("Main app to MQTT")
    global chairSensorAsezatThread
    if chairSensorAsezatThread is None:
        with flask_app.app_context():
            chairSensorAsezatThread = Thread(target=chair_sensor_asezat_thread)
            chairSensorAsezatThread.daemon = True
            print("Starting chairSensorAsezatThread")
            chairSensorAsezatThread.start()
            print("Started chairSensorAsezatThread")
    global chairSensorAvertismentThread
    if chairSensorAvertismentThread is None:
        with flask_app.app_context():
            chairSensorAvertismentThread = Thread(target=chair_sensor_avertisment_thread)
            chairSensorAvertismentThread.daemon = True
            print("Starting chairSensorAvertismentThread")
            chairSensorAvertismentThread.start()
            print("Started chairSensorAvertismentThread")

def chair_sensor_asezat_thread():
    global asezat
    while True:
        time.sleep(5)
        chance = random.randint(1, 100)
        if chance <= 1:
            asezat = not asezat
            print(f"Senzor scaun ---> Userul s-a {'asezat' if asezat else 'ridicat'}")
            from flask_app import user_asezat
            user_asezat.flask_app = flask_app
            with flask_app.app_context():
                user_asezat.setUserAsezat(asezat)
            mqtt.publish("scaun/user_asezat", asezat)

def chair_sensor_avertisment_thread():
    while True:
        time.sleep(60)
        from flask_app import user_asezat
        user_asezat.flask_app = flask_app
        with flask_app.app_context():
            userAsezat = user_asezat.getUserAsezat()
        if userAsezat is not None:
            if userAsezat["asezat"] == 1:
                lastUpdate = datetime.strptime(userAsezat["updated_on"], '%Y-%m-%d %H:%M:%S')
                duration = datetime.now() - lastUpdate
                if duration.total_seconds() > 30 * 60:
                    print(f"Senzor scaun ---> Userul nu s-a mai ridicat de 30 minute")
                    mqtt.publish("scaun/avertisment", b"Ati stat pe scaun prea mult. Luati o pauza.")