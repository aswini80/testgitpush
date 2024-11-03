import pymongo
client = pymongo.MongoClient("mongodb+srv://aswinikk:Radhe_2014@cluster0.lz6jw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
print(db)

d = {
    "name":"aswini",
    "email_id":"aswinikk@gmail.com",
    "surname":"khuntia"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)