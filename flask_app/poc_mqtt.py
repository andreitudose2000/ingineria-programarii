from flask import (Blueprint, g, request, jsonify)

bp = Blueprint('poc_mqtt', __name__, url_prefix='/poc-mqtt')

mqtt = None

@bp.route('/give-message', methods=(['GET']))
def giveMqttMessage():
    mqtt.publish("home/1", "2")
    return 'a', 200