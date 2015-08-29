from datetime import datetime
from weighttracker import db


class Inspiration(db.Document):
    phrase = db.StringField(required=True, unique=True)
    created_at = db.DateTimeField(default=datetime.now, required=True)
    updated_at = db.DateTimeField(default=datetime.now, required=True)
