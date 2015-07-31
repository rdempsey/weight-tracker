#!/usr/bin/env python

from flask import Flask, render_template, make_response, request, redirect, flash
from flask_wtf import Form
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
import os
from pymongo import MongoClient
import configparser
from datetime import datetime

app = Flask(__name__)
WTF_CSRF_ENABLED = True
app.secret_key = '2bN9UUaBpcjrxR'

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

# Measurements

class MeasurementsForm(Form):
  date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
  weight = StringField('Weight', validators=[DataRequired()])
  body_fat_percentage = StringField('Body Fat %')
  suprailiac = StringField('Suprailiac')
  abdominal = StringField('Abdominal')
  thigh = StringField('Thigh')

def get_measurement_history():
  client = connect()
  db = client.weighttracker
  my_measurements = [x for x in db.measurements.find()]
  return my_measurements

# Inspirations

class InspirationsForm(Form):
  phrase = StringField('I am the type of person who...', validators=[DataRequired()])

def get_inspirations():
  client = connect()
  db = client.weighttracker
  inspirations = [x for x in db.inspirations.find()]
  return inspirations


@app.route("/")
def index():
  response = make_response(render_template("index.html", title='Welcome'))
  return response

@app.route("/measurements")
def weight():
  form = MeasurementsForm()
  response = make_response(render_template("measurements.html", title='Track Your Measurements', measurements=get_measurement_history(), form=form))
  return response

@app.route("/add-measurements", methods=['POST'])
def write():
  form = MeasurementsForm()
  if form.validate_on_submit():
    client = connect()
    db = client.weighttracker
    created_at = str(datetime.now())
    # Get an oid
    oid = db.measurements.insert_one({
                                  "date":request.form.get("date"),
                                  "weight":request.form.get("weight"),
                                  "body_fat_percentage":request.form.get("body_fat_percentage"),
                                  "suprailiac":request.form.get("suprailiac"),
                                  "abdominal":request.form.get("abdominal"),
                                  "thigh":request.form.get("thigh"),
                                  "created_at":created_at
                                })
    # Redirect to the weight page
    return redirect ("/measurements")
  response = make_response(render_template("measurements.html", title='Measurements', measurements=get_measurement_history(), form=form))
  return response

@app.route("/inspirations")
def inspirations():
  form = InspirationsForm()
  response = make_response(render_template("inspirations.html", title="Inspirations", inspirations=get_inspirations(), form=form))
  return response

@app.route("/add-inspiration", methods=['POST'])
def write_inspiration():
  form = InspirationsForm()
  if form.validate_on_submit():
    client = connect()
    db = client.weighttracker
    created_at = str(datetime.now())
    # Get an oid
    oid = db.inspirations.insert_one({
                                  "phrase":request.form.get("phrase"),
                                  "created_at":created_at,
                                })
    # Redirect to the weight page
    return redirect ("/inspirations")
  response = make_response(render_template("inspirations.html", title='Inspirations', inspirations=get_inspirations(), form=form))
  return response

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)