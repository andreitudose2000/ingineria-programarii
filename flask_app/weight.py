from datetime import datetime
from flask import (Blueprint, g, request, jsonify)
from flask_app.db import get_db
import random

bp = Blueprint('weight', __name__, url_prefix='/weight')

@bp.route('/measure', methods=(['GET']))
def measure_weight():
    weight = random.randint(70, 100)
    db = get_db()
    db.execute(
        "INSERT INTO user_weight (mass) VALUES (?)",
        (weight,),
    )
    db.commit()
    return jsonify(weight = weight), 200

@bp.route('/history', methods=(['GET']))
def report_weight():
    db = get_db()
    entrys = db.execute(
        "SELECT * FROM user_weight", ()
    ).fetchall()
    res = []
    for x in entrys:
        res.append({'id' : x['id'], 'mass' : x['mass'], 'updated_on' : x['updated_on']})
    return jsonify(res), 200
