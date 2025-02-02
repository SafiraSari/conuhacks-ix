import os

from flask import Flask, render_template # type: ignore
from backend import *

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, template_folder='frontend', static_folder='frontend')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    #  TODO: make this more dynamic later on. could use a dictionary in set_up_data and take the path within app.route
    @app.route('/login')
    def login():
        return render_template(set_up_data.login_page_file)
    
    @app.route('/homepage')
    def homepage():
        return render_template(set_up_data.homepage_file)
    
    @app.route('/userpage')
    def user_page():
        return render_template(set_up_data.user_page_file)
    
    db.init_app(app)

    return app