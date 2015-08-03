from datetime import datetime
from flask import url_for
from weighttracker import db

class Measurement(db.Document):
  date = db.StringField(required=True, unique=True, max_length=100)
  weight = db.DecimalField()
  body_fat_percentage = db.DecimalField()
  suprailiac = db.DecimalField()
  abdominal = db.DecimalField()
  thigh = db.DecimalField()
  created_at = db.DateTimeField(default=datetime.now, required=True)
  updated_at = db.DateTimeField(default=datetime.now, required=True)