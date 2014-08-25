import pymongo
from bangx2.settings import MONGO_HOST
from bangx2.settings import MONGO_PORT
from bangx2.settings import MONGO_DB

class MongoClient():
    client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[MONGO_DB]
