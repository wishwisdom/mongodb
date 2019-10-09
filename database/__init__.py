import pymongo

IP = 'localhost'
PORT = 27017
DATABASE = 'local'

conn = pymongo.MongoClient(IP, PORT)
db = conn.get_database(DATABASE)
