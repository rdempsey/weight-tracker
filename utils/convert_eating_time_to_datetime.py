#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime

# def fixTime(host, port, database, collection, attr, date_format):
    #host is where the mongodb is hosted eg: "localhost"
    #port is the mongodb port eg: 27017
    #database is the name of database eg : "test"
    #collection is the name of collection eg : "test_collection"
    #attr is the column name which needs to be modified
    #date_format is the format of the string eg : "%Y-%m-%d %H:%M:%S.%f"
    #http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

attr = 'eating_time'

client = MongoClient('localhost', 27017)
db = client['weighttracker']
col = db['foodjournal']
for obj in col.find():
    if obj[attr]:
        if type(obj[attr]) is not datetime:
            time = datetime.strptime(obj[attr],"%m/%d/%Y %H:%M %p")
            col.update({'_id':obj['_id']},{'$set':{attr : time}})