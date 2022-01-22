from array import array
from datetime import datetime
from flask import (Blueprint, g, request, jsonify)
from flask_app.db import get_db

bp = Blueprint('poc', __name__, url_prefix='/poc')

@bp.route('/json-response', methods=(['GET']))
def jsonResponse():
    return jsonify({'test': 'sucessful'}), 200

@bp.route('/json-response', methods=(['POST']))
def jsonResponse2():
    if 'ma' not in request.json:
        return jsonify(probleme = "asta e nu s-a putut ai nevoie de proprietatea \'ma\'"), 400
    return jsonify({'eu': f'{request.json["ma"]} aodwiubo', "dar" : "nu e imposibil"}), 200

# 500 response only prod
@bp.route('/json-response-500', methods=(['POST']))
def jsonResponse3():
    return jsonify({'eu': f'{request.json["mawdawdawdawda"]} aodwiubo', "dar" : "nu e imposibil"}), 200


@bp.route('/add-to-db', methods=(['POST']))
def addToDb():
    if not request.json:
        return jsonify(probleme = "hai ca nu mere fara json"), 400
    if 'some_text' not in request.json:
        return jsonify(probleme = "lipseste 'some_text'"), 400
    if 'another_text' not in request.json:
        return jsonify(probleme = "lipseste 'another_text'"), 400
    if 'a_date' not in request.json:
        return jsonify(probleme = "lipseste 'a_date'"), 400
    
    try:
        date = datetime.strptime(request.json['a_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        return jsonify(probleme = "data domnul meu"), 400
    
    db = get_db()
    try:
        db.execute(
            "INSERT INTO test (some_text, another_text, a_date) VALUES (?, ?, ?)",
            (request.json['some_text'], request.json['another_text'], date),
        )
        db.commit()
    except db.IntegrityError:
        return jsonify(probleme = "some_text is unique"), 500
    
    return jsonify(no_problem = "ok"), 200

@bp.route('/get-from-db', methods=(['GET']))
def getFromDb():
    if 'id' not in request.args:
        return jsonify(probleme = "lipseste 'id'"), 400
    id = request.args['id']
    db = get_db()
    entry = db.execute(
            'SELECT * FROM test WHERE id = ?', (id) # id, some_text, another_text
        ).fetchone()
    return jsonify(no_problem = entry['some_text']), 200

@bp.route('/get-all-from-db', methods=(['GET']))
def getFromDb2():
    db = get_db()
    entrys = db.execute(
            'SELECT id, some_text, another_text FROM test'
        ).fetchall()
    res = []
    for x in entrys:
        res.append({'id' : x['id'], 'some_text' : x['some_text'], 'another_text' : x['another_text']})
    return jsonify(res), 200