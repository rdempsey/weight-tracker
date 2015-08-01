# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import configparser

app = Flask(__name__)
# Security
WTF_CSRF_ENABLED = True
app.config['SECRET_KEY'] = '2bN9UUaBpcjrxR'

# App Config
config = configparser.ConfigParser()
config.read('config/config.ini')

app.config['MONGODB_DB'] = config['MongoDB']['db_name']
app.config['MONGODB_HOST'] = config['MongoDB']['host']
app.config['MONGODB_PORT'] = int(config['MongoDB']['port'])
app.config['MONGODB_USERNAME'] = config['MongoDB']['username']
app.config['MONGODB_PASSWORD'] = config['MongoDB']['password']

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from weighttracker.views.measurement_views import measurements
    app.register_blueprint(measurements)
    from weighttracker.views.inspiration_views import inspirations
    app.register_blueprint(inspirations)

register_blueprints(app)


if __name__ == '__main__':
    app.run()