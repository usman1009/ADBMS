import pymongo
url="mongodb://localhost:27017"
client=pymongo.MongoClient(url)
db=client["bank"]
coll=db["customers"]

#coll.insert_one({"_id":1,"name":{"fname":"abhinand","lname":"narayanan"},"address":"parambath","phone":{"ph1":12345,"ph2":54321},"adhaar_no":5468594935,"branch":"sreekaryam"})

#list=[{"_id":2,"name":{"fname":"sachin","lname":"m"},"address":"meledath","ph1":9999999999,"adhaar_no":8765594935,"branch":"calicut"},{"_id":3,"name":{"fname":"ashaad","lname":"mohd"},"address":"kazhakkootam","phone":{"ph1":6547657345,"ph2":768646321},"adhaar_no":9878657594935,"branch":"malappuram"}]
#coll.insert_many(list)

#for x in coll.find({"branch":"sreekaryam"}):
	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["address"]+" "+str(x["phone"]["ph1"])+" "+str(x["phone"]["ph2"])+" "+str(x["adhaar_no"])+" "+x["branch"])
#for x in coll.find({"address":"kazhakkootam"}):
	#print(x["name"]["fname"]+" "+x["name"]["lname"])
myquery={"ph1":9999999999}
newvalue={"$set":{"name.lname":"meledath"}}
for x in coll.find({"ph1":9999999999}):
	print(x["name"]["fname"]+" "+x["name"]["lname"])