import pymongo, json, urllib2
from pprint import pprint

connection = pymongo.MongoClient('149.89.150.100')
db=connection.gaoJ-soeW
collection=db.events

u=urllib2.urlopen("http://www.vizgr.org/historical-events/search.php?format=json&begin_date=20000101&end_date=20151231&lang=en")
data=u.read()
eventDict=json.loads(data)
