connection = pymongo.MongoClient('149.89.150.100')
db = connection.test
collection = db.restaurants

def boroughSearch(borough):
    results = collection.find({'borough' : borough})
    return results

print boroughSearch('Manhattan')
