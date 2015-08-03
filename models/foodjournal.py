from datetime import datetime
from flask import url_for
from weighttracker import db

class Foodjournal(db.Document):

  mood_levels = (('Not at all','Not at all'),
                 ('A little','A little'),
                 ('Moderately','Moderately'),
                 ('Quite a Lot','Quite a Lot'),
                 ('Extremely','Extremely'))

  mood_choices = (('Active','Active'),
                  ('Alert','Alert'),
                  ('Anger','Anger'),
                  ('Annoyed','Annoyed'),
                  ('Anxious','Anxious'),
                  ('Bad Tempered','Bad Tempered'),
                  ('Bewildered','Bewildered'),
                  ('Bitter','Bitter'),
                  ('Blue','Blue'),
                  ('Bushed','Bushed'),
                  ('Carefree','Carefree'),
                  ('Cheerful','Cheerful'),
                  ('Confused','Confused'),
                  ('Deceived','Deceived'),
                  ('Desperate','Desperate'),
                  ('Discouraged','Discouraged'),
                  ('Efficient','Efficient'),
                  ('Energetic','Energetic'),
                  ('Exhausted','Exhausted'),
                  ('Fatigued','Fatigued'),
                  ('Forgetful','Forgetful'),
                  ('Full of Pep','Full of Pep'),
                  ('Furious','Furious'),
                  ('Gloomy','Gloomy'),
                  ('Grouchy','Grouchy'),
                  ('Guilty','Guilty'),
                  ('Helpless','Helpless'),
                  ('Hopeless','Hopeless'),
                  ('Listless','Listless'),
                  ('Lively','Lively'),
                  ('Lonely','Lonely'),
                  ('Miserable','Miserable'),
                  ('Muddled','Muddled'),
                  ('Nervous','Nervous'),
                  ('On Edge','On Edge'),
                  ('Panicky','Panicky'),
                  ('Peeved','Peeved'),
                  ('Ready to Fight','Ready to Fight'),
                  ('Rebellious','Rebellious'),
                  ('Relaxed','Relaxed'),
                  ('Resentful','Resentful'),
                  ('Restless','Restless'),
                  ('Sad','Sad'),
                  ('Shaky','Shaky'),
                  ('Sluggish','Sluggish'),
                  ('Sorry for Things Done','Sorry for Things Done'),
                  ('Spiteful','Spiteful'),
                  ('Tense','Tense'),
                  ('Terrified','Terrified'),
                  ('Unable to Concentrate','Unable to Concentrate'),
                  ('Uncertain About Things','Uncertain About Things'),
                  ('Uneasy','Uneasy'),
                  ('Unhappy','Unhappy'),
                  ('Unworthy','Unworthy'),
                  ('Vigorous','Vigorous'),
                  ('Weary','Weary'),
                  ('Worn Out','Worn Out'),
                  ('Worthless','Worthless'))

  eating_time = db.StringField(required=True, unique=True, max_length=100)
  where_i_ate = db.StringField()
  what_was_eaten = db.StringField()
  what_was_drank = db.StringField()
  level_of_mood_before_food = db.StringField(choices=mood_levels)
  mood_before_food = db.StringField(choices=mood_choices)
  level_of_mood_after_food = db.StringField(choices=mood_levels)
  mood_after_food = db.StringField(choices=mood_choices)
  created_at = db.DateTimeField(default=datetime.now, required=True)
  updated_at = db.DateTimeField(default=datetime.now, required=True)