from datetime import datetime
from tokenize import Number
from unicodedata import numeric
from flask import (Blueprint, g, request, jsonify, current_app)
from flask_app.db import get_db
import json

bp = Blueprint('heat', __name__, url_prefix='/heat')

temp = None
mqtt = None
app = None

@bp.route('/set', methods=(['POST']))
def add_temps():
    if not request.json:
        return jsonify(probleme = "Lipseste body"), 400
    if 'headrest' not in request.json:
        return jsonify(probleme = "Valoare pt headrest lipseste"), 400
    if 'backrest' not in request.json:
        return jsonify(probleme = "Valoare pt backrest lipseste"), 400
    if 'armrest' not in request.json:
        return jsonify(probleme = "Valoare pt armrest lipseste"), 400
    if 'bumrest' not in request.json:
        return jsonify(probleme = "Valoare pt bumrest lipseste"), 400
    moment = datetime.utcnow()
    db = get_db()
    try:
        db.execute(
            "INSERT INTO heat (headrest, backrest, armrest, bumrest, moment) VALUES (?, ?, ?, ?, ?)",
            (request.json['headrest'], request.json['backrest'], request.json['armrest'], request.json['bumrest'], moment),
        )
        db.commit()
    except db.IntegrityError:
        return jsonify(probleme = "i dunno"), 500
    
    if temp is not None:
        adjust_temp(temp, request.json['headrest'], request.json['backrest'], request.json['armrest'], request.json['bumrest'])

    return jsonify(probleme = "ok"), 200

def adjust_temp(temp, headrest, backrest, armrest, bumrest):
    mqtt.publish("scaun/incalzire", f'sezut: {bumrest >= temp}; spatar: {backrest >= temp}; headrest: {headrest >= temp}; armrest: {armrest >= temp}')
    mqtt.publish("scaun/incalzire", json.loads(sezut=bumrest >= temp, spatar=backrest >= temp, headrest=headrest >= temp, armrest=armrest >= temp))

def new_temp(temper):
    with app.app_context():
        temp = temper
        db = get_db()
        entry = db.execute(
                "SELECT * FROM heat m1 WHERE m1.moment = (SELECT MAX(m2.moment) from heat m2)", ()
            ).fetchone()
    if entry is None:
        return

    adjust_temp(temp, entry['headrest'], entry['backrest'], entry['armrest'], entry['bumrest'])
