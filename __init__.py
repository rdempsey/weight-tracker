# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import configparser
from .momentjs import momentjs

app = Flask(__name__)
# Security
WTF_CSRF_ENABLED = True
app.config['SECRET_KEY'] = '2bN9UUaBpcjrxR'
app.jinja_env.globals['momentjs'] = momentjs

# App Config
config = configparser.ConfigParser()
config.read('config/config.ini')

app.config['MONGODB_SETTINGS'] = {
  'db': config['MongoDB']['db_name'],
  'host': config['MongoDB']['host'],
  'port': int(config['MongoDB']['port']),
  'username': config['MongoDB']['username'],
  'password': config['MongoDB']['password']}

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from weighttracker.views.measurement_views import measurements
    app.register_blueprint(measurements)
    from weighttracker.views.inspiration_views import inspirations
    app.register_blueprint(inspirations)
    from weighttracker.views.foodjournal_views import foodjournals
    app.register_blueprint(foodjournals)

register_blueprints(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def catch_all(path):
    return render_template('index.html')


if __name__ == '__main__':
  app.run()