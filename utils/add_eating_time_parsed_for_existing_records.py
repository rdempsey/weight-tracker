#!/usr/bin/env python

from pymongo import MongoClient
import parsedatetime
from datetime import datetime
from time import mktime

client = MongoClient('localhost', 27017)
db = client['weighttracker']
col = db['foodjournal']
for obj in col.find():
    if obj['eating_time']:
        # time = datetime.strptime(obj[attr],"%m/%d/%Y %H:%M %p")
        # col.update({'_id':obj['_id']},{'$set':{attr : time}})
        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(obj['eating_time'])
        eating_time_parsed = datetime.fromtimestamp(mktime(time_struct))
        col.update({'_id':obj['_id']},{'$set':{'eating_time_parsed' : eating_time_parsed}})

