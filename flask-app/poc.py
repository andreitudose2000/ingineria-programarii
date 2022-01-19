from flask import (Blueprint, g, request, jsonify)

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