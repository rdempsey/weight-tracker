from datetime import datetime
from flask import url_for
from weighttracker import db

class Exercisejournal(db.Document):

  motivation_levels = (('---','---'),
                       ('Not in the mood', 'Not in the mood'),
                       ('Tired', 'Tired'),
                       ('Average', 'Average'),
                       ('Pumped Up', 'Pumped Up'))

  exercise_locations = (('---','---'),
                  ('Gym','Gym'),
                  ('Home','Home'),
                  ('Home Gym','Home Gym'),
                  ('Hotel Gym','Hotel Gym'),
                  ('Office Gym','Office Gym'),
                  ('Outdoors','Outdoors'),
                  ('Other','Other'))

  exercise_time = db.StringField(required=True, unique=True, max_length=100)
  where_i_exercised = db.StringField(choices=exercise_locations)
  exercises_performed = db.StringField()
  exercise_notes = db.StringField()
  motivation_level_before_exercise = db.StringField(choices=motivation_levels)
  motivation_level_after_exercise = db.StringField(choices=motivation_levels)
  exercise_time_parsed = db.DateTimeField()
  created_at = db.DateTimeField(default=datetime.now(), required=True)
  updated_at = db.DateTimeField(default=datetime.now(), required=True)