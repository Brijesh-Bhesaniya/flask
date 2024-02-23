import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['test_db_2']
mycol = mydb['users']