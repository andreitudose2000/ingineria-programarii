from flask_app.db import get_db

flask_app = None

def setUserAsezat(asezat):
    try:
        print("##Updated in db ",asezat)
        db = get_db()
        db.execute("INSERT INTO user_asezat (asezat) VALUES (?)",
                   (int(asezat),))
        db.commit()
        return True
    except Exception as e:
        print("Exceptie set: ", e)
        return False

def getUserAsezat():
    try:
        db = get_db()
        userAsezat = db.execute(
            'SELECT id, asezat, updated_on \
            FROM user_asezat \
            ORDER BY updated_on DESC'
        ).fetchone()

        return userAsezat
    except Exception as e:
        print("Exceptie get: ", e)
        return None