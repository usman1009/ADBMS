import pymongo
url="mongodb://localhost:27017"
c=pymongo.MongoClient(url)
db=c["exams"]
coll=db["students"]


lis=[{"_id":1,"name":"Anjali","place":"Kollam","Phone":"8582639562","vaccination_status":"Both vaccinated","RTPCR":"negative","Lab_mark":
      {"internal":30,"external":45},"department":"MCA"},
{"_id":2,"name":"Anuradha","place":"Varkala","Phone":"9992639562","vaccination_status":"Both vaccinated","RTPCR":"negative","Lab_mark":
 {"internal":40,"external":48},"department":"civil"},{"_id":3,"name":"Bismiya","place":"Kollam","Phone":"9446639562","vaccination_status":"Not vaccinated","RTPCR":"positive","Lab_mark":{"internal":50,"external":39},"department":"MCA"},
{"_id":4,"name":"Vimal","place":"Ernakulam","Phone":"8582639568","vaccination_status":"first dose only","RTPCR":"negative","Lab_mark":
 {"internal":40,"external":42},"department":"Civil"},{"_id":5,"name":"Vivek","place":"Kollam","Phone":"8582639777","vaccination_status":"Both vaccinated","RTPCR":"negative","Lab_mark":{"internal":50,"external":50},"department":"MCA"}]
#coll.insert_many(lis)

#for x in coll.find({"vaccination_status":"Both vaccinated"}):
	#print(x["name"]+ " "+str(x["Phone"]))

#for x in coll.find({"department":"MCA"}).sort("Lab_mark.external",-1).limit(2):
	#print(x["name"]+ " "+str(x["Phone"]))

#for x in coll.find({"name":{"$regex":"^A"}}):
	#print(x["name"]+ " "+str(x["_id"])+ " "+x["department"])

#coll.update({"_id":4,"_id":3},{"$set":{"vaccination_status":"Both vaccinated"}},{"multi":"true"})
#for x in coll.find({"_id":4,"_id":3}):	

       	#print(x["name"]+ " "+x["vaccination_status"] ) 

#myquery={"_id":4}
#newvalues={"$set":{"vaccination_status":"Both vaccinated"}}
#coll.update_many(myquery,newvalues)
#for x in coll.find({"_id":4}):	

       	#print(str(x["_id"])+" "+x["name"]+ " "+x["vaccination_status"] ) 
for x in coll.find().sort("Lab_mark.external",-1):
	print(x["name"]+ " "+str(x["Lab_mark"]["external"]) )