from datetime import datetime
from math import fabs
from tokenize import Number
from unicodedata import numeric
from flask import (Blueprint, g, request, jsonify, current_app)
from flask_app.db import get_db
import json

bp = Blueprint('heat', __name__, url_prefix='/heat')

temp = None
mqtt = None
app = None

def add_to_db(head_rest, back_rest, arm_rest, bum_rest):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO heat (head_rest, back_rest, arm_rest, bum_rest) VALUES (?, ?, ?, ?)",
            (head_rest, back_rest, arm_rest, bum_rest),
        )
        db.commit()
    except db.IntegrityError:
        return False
    return True

@bp.route('/', methods=(['POST']))
def add_temps():
    if not request.json:
        return jsonify(message = "Lipseste body"), 400
    if 'head_rest' not in request.json:
        return jsonify(message = "Valoare pt head_rest lipseste"), 400
    if 'back_rest' not in request.json:
        return jsonify(message = "Valoare pt back_rest lipseste"), 400
    if 'arm_rest' not in request.json:
        return jsonify(message = "Valoare pt arm_rest lipseste"), 400
    if 'bum_rest' not in request.json:
        return jsonify(message = "Valoare pt bum_rest lipseste"), 400
    
    if not add_to_db(request.json['head_rest'], request.json['back_rest'], request.json['arm_rest'], request.json['bum_rest']):
        return jsonify(message = "Db problem"), 500
    
    if temp is not None:
        adjust_temp(temp, request.json['head_rest'], request.json['back_rest'], request.json['arm_rest'], request.json['bum_rest'])

    return jsonify(message = "ok"), 200



def adjust_temp(temp, headrest, backrest, armrest, bumrest):
    mqtt.publish("scaun/incalzire", json.loads(sezut=bumrest >= temp, spatar=backrest >= temp, headrest=headrest >= temp, armrest=armrest >= temp))

def fetch_last_settings():
    db = get_db()
    entry = db.execute(
            "SELECT * FROM heat m1 WHERE m1.updated_on = (SELECT MAX(m2.updated_on) from heat m2)", ()
        ).fetchone()
    return entry

def new_temp(temper):
    with app.app_context():
        temp = temper
        entry = fetch_last_settings()
        
    if entry is None:
        return

    adjust_temp(temp, entry['head_rest'], entry['back_rest'], entry['arm_rest'], entry['bum_rest'])
