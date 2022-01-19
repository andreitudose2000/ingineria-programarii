import os

from flask import Flask, jsonify

# error functions
def page_not_found(e):
        return jsonify(error=str(e)), 404

def internal(e):
        return jsonify(error=str(e)), 500

# app factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask-app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

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