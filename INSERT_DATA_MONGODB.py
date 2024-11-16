import pymongo
cliet=pymongo.MongoClient("mongodb://localhost:27017")
db=cliet["ACT_DB"]
coll=db["STU_DB"]
data=[{"SID":501,"SNAME":"SANDEESHA","SCOURSE":"AIML","SPHONE":"9381508534"},
      {"SID":502,"SNAME":"SARU","SCOURSE":"SELENIUM","SPHONE":"9121743133"},
      {"SID": 503, "SNAME": "THARUN", "SCOURSE": "PYTHON", "SPHONE": "9390685200"}]
X=coll.insert_many(data)
print("data has been inserted into desired collection:\n")
print("primary keys:\n",X.inserted_ids)

