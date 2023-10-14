from flask import Flask
from flask_app.controllers.User_controller import user
from flask_app.controllers.Thought_controller import thoughts
app = Flask(__name__, template_folder='views')
app.register_blueprint(user)
app.register_blueprint(thoughts)
app.secret_key = 's3cr3t-p@55w0rd'
