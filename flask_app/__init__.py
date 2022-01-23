import os

from flask import Flask, jsonify

# error functions
def page_not_found(e):
        return jsonify(error=str(e)), 404

def internal(e):
        return jsonify(error=str(e)), 500

# app factory
def create_app(test_config=None, db_file=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=(db_file is not None))

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flask-app.sqlite'),
        )
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    if db_file is not None:
        app.config["DATABASE"] = db_file

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # error handling
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal)

    # database
    from . import db
    db.init_app(app)
    
    # Url to check if running
    @app.route('/')
    def hello():
        return 'Hello, World!'

    # Adding blueprints/controllers
    from . import poc
    app.register_blueprint(poc.bp)

    return app