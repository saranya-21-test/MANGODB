import pymongo
cliet=pymongo.MongoClient("mongodb://localhost:27017")
db=cliet["ACT_DB"]
coll=db["STU_DB"]
query={"SID":503}
coll.delete_one(query)
print("ur record or document is deleted succesfully")