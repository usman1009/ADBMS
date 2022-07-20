import pymongo
url="mongodb://localhost:27017"
client=pymongo.MongoClient(url)
db=client["sales"]
coll=db["order"]

#coll.insert_one({"_id":"o1","year":2008,"cost":"100dollar","order":{"product1":{"p_id":"p1","colurs":"3","qunt":10},"product2":{"p_id":"p2","colurs":"2","qunt":10}},"paid_status":"Y"})
list=[{"_id":"o3","year":2009,"cost":"10","order":{"product1":{"p_id":"p1","colurs":"4","qunt":50},"product2":{"p_id":"p2","colurs":"40","qunt":60}},"paid_status":"N"},
{"_id":"o2","year":2010,"cost":"15","order":{"product1":{"p_id":"p1","colurs":"45","qunt":170},"product2":{"p_id":"p2","colurs":"72","qunt":810}},"paid_status":"Y"},
{"_id":"o4","year":2008,"cost":"30","order":{"product1":{"p_id":"p1","colurs":"36","qunt":610},"product2":{"p_id":"p2","colurs":"27","qunt":610}},"paid_status":"N"}]

#coll.insert_many(list)

#for x in coll.find():
 #print(x["_id"]+" "+str(x["year"])+" "+str(x["cost"])+" "+x["order"]["product1"]["p_id"]+" "+x["order"]["product1"]["colurs"]+" "+str(x["order"]["product1"]["qunt"])+" "+x["order"]["product2"]["p_id"]+" "+x["order"]["product2"]["colurs"]+ " "+str(x["order"]["product2"]["qunt"]))

#for x in coll.find({"order.product2.p_id":"p2"}):
	#print(x["_id"]+" "+str(x["year"])+" "+str(x["cost"])+" "+x["order"]["product2"]["p_id"]+" "+x["order"]["product2"]["colurs"]+" "+str(x["order"]["product2"]["qunt"]))

#for x in coll.find({"cost":{"$lt":18}}):
	#print(x["_id"]+" "+str(x["year"])+" "+str(x["cost"]))

#for x in coll.find({"paid_status":"Y","year":{"$lt":2009}}):
	#print(x["_id"]+" "+str(x["year"])+" "+str(x["cost"]))
#for x in coll.find({"cost.currency":"rupees"}):
	#print(x["_id"]+" "+str(x["year"])+" "+str(x["cost"]["price"]))

for x in coll.find({"cost.currency":"euro","cost.price":{"$lt":18}}):
	print(x["_id"]+" "+str(x["year"])+" "+str(x["cost"]["price"]))
