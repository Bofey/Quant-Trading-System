from pymongo import MongoClient, UpdateOne

DB = MongoClient('mongodb://127.0.0.1:27017')['my_quant']