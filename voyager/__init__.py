import os

from flask import Flask
import flask_login
from flask_login import LoginManager, UserMixin, login_required
from voyager import db, views



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
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

    login_manager = LoginManager()
    login_manager.init_app(app)
    views.init_app(app)



    @login_manager.request_loader
    def load_user(request):
        token = request.headers.get('Authorization')
        if token is None:
            token = request.args.get('token')

        if token is not None:
            username,password = token.split(":") # naive token
            user_entry = User.get(username)
            if (user_entry is not None):
                user = User(user_entry[0],user_entry[1])
                if (user.password == password):
                    return user
        return None
    @app.route("/",methods=["GET"])
    def index():
        return Response(response="Hello World!",status=200)


    @app.route("/protected/",methods=["GET"])
    @login_required
    def protected():
        return Response(response="Hello Protected World!", status=200)
    # login_manager = flask_login.LoginManager()

    # login_manager.init_app(app)
    # class User(flask_login.UserMixin):
    #     pass


    # @login_manager.user_loader
    # def user_loader(email):
    #     if email not in users:
    #         return

    #     user = User()
    #     user.id = email
    #     return user


    # @login_manager.request_loader
    # def request_loader(request):
    #     email = request.form.get('email')
    #     if email not in users:
    #         return

    #     user = User()
    #     user.id = email

    #     # DO NOT ever store passwords in plaintext and always compare password
    #     # hashes using constant-time comparison!
    #     user.is_authenticated = request.form['password'] == users[email]['password']

    #     return user
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

