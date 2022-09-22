from flask import Flask
from politiky.extensions import configuration

app = Flask(__name__)

configuration.init_app(app)
configuration.load_extension(app)

print(app.config['APPNAME'])

