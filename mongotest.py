import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://rudra22:rudra22@cluster1.6b2tmjv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "Name":"Darshan",
    "email":"darshan@gmail.com",
    "address":"pune"
}

dk= client["mongotest"]
ap=dk['abatlas']
ap.insert_one(d)