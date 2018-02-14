import pymongo
from pprint import pprint

connection = pymongo.MongoClient('149.89.150.100')
db = connection.test
collection = db.restaurants

def boroughSearch(borough):
    results = collection.find({'borough' : borough})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

def zipCodeSearch(zipcode):
    results=collection.find({'address.zipcode':zipcode})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

def zipcodeGrade(zipcode, grade):
    results=collection.find({'address.zipcode':zipcode, 'grades.grade':grade})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

def score(zipcode, score):
    results=collection.find({'address.zipcode':zipcode, 'grades.score':{$lt: score}})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#print boroughSearch('Manhattan')
#print zipCodeSearch('10017')
#print zipcodeGrade('10017', 'B')
print score('10017', 23)
