import pymongo
url="mongodb://localhost:27017"
client=pymongo.MongoClient(url)
db=client["house"]
coll=db["person"]

#coll.insert_one({"_id":1,"name":{"fname":"abhinand","lname":"narayanan"},"address":{"address1":{"hname":"parambath","street":"calicut","city":"calicut"},"address2":{"hname":"abc","street":"cal","city":"calic"}}})
#list=[{"_id":2,"name":{"fname":"Arun","lname":"n"},"address":{"address1":{"hname":"kottakkaran","street":"malappuram","city":"malappuram"},"address2":{"hname":"fdsfrtg","street":"malap","city":"mal"}}},
#coll.insert_one({"_id":3,"name":{"fname":"Gopal","lname":"n"},"address":{"address1":{"hname":"meledath","street":"xstreet","city":"tvm"},"address2":{"hname":"gfgfg","street":"gfhg","city":"tvm"}}})
#coll.insert_many(list)

#for x in coll.find({"name.fname":"Arun"}):
   	#print(x["name"]["fname"]+ " "+x["name"]["lname"]+" "+x["address"]["address1"]["hname"]+" "+x["address"]["address1"]["street"]+ " "+x["address"]["address1"]["city"]+ " "+x["address"]["address2"]["hname"]+" "+x["address"]["address1"]["street"]+" "+x["address"]["address1"]["city"])

myquery={"address.address1.street":"xstreet"}
newvalues={"$set":{"address.address1.street":"lovedate"}}
coll.update_many(myquery,newvalues)
for x in coll.find({"address.address1.street":"lovedate"}):
	print(x["name"]["fname"]+ " "+x["name"]["lname"]+" "+x["address"]["address1"]["hname"]+" "+x["address"]["address1"]["street"]+ " "+x["address"]["address1"]["city"]+ " "+x["address"]["address2"]["hname"]+" "+x["address"]["address2"]["street"]+" "+x["address"]["address2"]["city"])
	
