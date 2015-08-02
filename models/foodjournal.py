from datetime import datetime
from flask import url_for
from weighttracker import db

class Foodjournal(db.Document):
  eating_time = db.DateTimeField(required=True, unique=True)
  location_at_time = db.StringField()
  what_was_eaten = db.StringField()
  what_was_drank = db.StringField()
  mood_before = db.StringField()
  mood_after = db.StringField()
  created_at = db.DateTimeField(default=datetime.now, required=True)
  updated_at = db.DateTimeField(default=datetime.now, required=True)