#!/usr/bin/env python

from pymongo import MongoClient
import parsedatetime
from datetime import datetime
from time import mktime

client = MongoClient('localhost', 27017)
db = client['weighttracker']
col = db['measurement']
for obj in col.find():
    if obj['date']:
        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(obj['date'])
        timestamp_update = datetime.fromtimestamp(mktime(time_struct))
        col.update({'_id':obj['_id']},{'$set':{
                                                'measurement_time': timestamp_update,
                                                'updated_at' : timestamp_update,
                                                'created_at': timestamp_update
                                                }})

