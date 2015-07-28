#!/usr/bin/env python

from flask import Flask, render_template, make_response, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
import os
from pymongo import MongoClient
import configparser

app = Flask(__name__)
app.secret_key = '2bN9UUaBpcjrxR'
Bootstrap(app)

def connect():
  # Read the config file and get the goodies
  config = configparser.ConfigParser()
  config.read('config/config.ini')

  # Set all of the variables we need
  db_host = config['MongoDB']['host']
  db_port = int(config['MongoDB']['port'])
  db_user = config['MongoDB']['username']
  db_password = config['MongoDB']['password']
  db_name = config['MongoDB']['db_name']

  client = MongoClient(db_host,db_port)
  client.weighttracker.authenticate(db_user, db_password, source=db_name)
  return client

class MeasurementsForm(Form):
  date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
  weight = StringField('Weight', validators=[DataRequired()])
  body_fat_percentage = StringField('Body Fat %')
  suprailiac = StringField('Suprailiac')
  abdominal = StringField('Abdominal')
  thigh = StringField('Thigh')

def get_weight_history():
  # Connect to the database
  client = connect()
  # Get a database
  db = client.weighttracker
  # Get all of the weights in the collection
  my_weights = [x for x in db.weights.find()]
  # Return the list of weights
  return my_weights


@app.route("/")
def index():
  form = MeasurementsForm()
  response = make_response(render_template("index.html", weights=get_weight_history(), form=form))
  return response

@app.route("/add-weight", methods=['POST'])
def write():
  form = MeasurementsForm()
  if form.validate_on_submit():
    client = connect()
    db = client.weighttracker
    # Get an oid
    oid = db.weights.insert_one({
                                  "date":request.form.get("date"),
                                  "weight":request.form.get("weight"),
                                  "body_fat_percentage":request.form.get("body_fat_percentage"),
                                  "suprailiac":request.form.get("suprailiac"),
                                  "abdominal":request.form.get("abdominal"),
                                  "thigh":request.form.get("thigh")
                                })
    # Redirect to the home page
    return redirect ("/")
  response = make_response(render_template("index.html", weights=get_weight_history(), form=form))
  return response

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)