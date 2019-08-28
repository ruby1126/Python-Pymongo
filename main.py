from pymongo import MongoClient


__uri = "mongodb://{}:{}@{}:{}/".format('root', 'password', '127.0.0.1', 27017)
__mongodb_client = MongoClient(__uri)
db = __mongodb_client['dbname']

find = db.collection.find()
insert_many = db.collection.insert_many([{"content":"value"},{"content":"value2"}])
insert_one = db.collection.insert_one({"content":"value"})
update_one = db.collection.update_one({'_id':"id"},{"$set": {"content":"new value"}})
remove = db.collection.remove({"_id":"id"})
