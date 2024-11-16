import pymongo
cliet=pymongo.MongoClient("mongodb://localhost:27017")
db=cliet["ACT_DB"]
coll=db["STU_DB"]
query={"SID":503}
new_values={"$set":{"SNAME":"sandy"}}
coll.update_one(query,new_values)
for i in coll.find():
    print("student details:\n",i)