import pymongo
url="mongodb://localhost:27017"
c=pymongo.MongoClient(url)
db=c["collegess"]
coll=db["stud_lists"]

list=[{
  "_id": 1,
  "name": {
    "fname": "Athira",
    "lname": "Krishnan"
  },
  "address": {
    "house_name": "Ambadi",
    "city": "Kollam"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 80,
  "grade": "A",
  "phone": {
    "type": "mobile",
    "no": 9896321450
  }
},{
  "_id": 2,
  "name": {
    "fname": "Arya",
    "lname": "S"
  },
  "address": {
    "house_name": "M.B.S.Bhavan",
    "city": "Varkala"
  },
  "gender": "female",
  "course": "Computer Science",
  "mark": 90,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 9446321420
  }
},{
  "_id": 3,
  "name": {
    "fname": "Varun",
    "lname": "Nair"
  },
  "address": {
    "house_name": "Koustubham",
    "city": "Thiruvananthapuram"
  },
  "gender": "male",
  "course": "MCA",
  "mark": 70,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04712662690"
  }
},{
  "_id": 4,
  "name": {
    "fname": "Vidhya",
    "lname": "S"
  },
  "address": {
    "house_name": "MRS House",
    "city": "Kadakkavoor"
  },
  "gender": "female",
  "course": "Civil",
  "mark": 85,
  "grade": "A",
  "phone": {
    "type": "mobile",
    "no": 8146321420
  }
},{
  "_id": 5,
  "name": {
    "fname": "Karthik",
    "lname": "MS"
  },
  "address": {
    "house_name": "Devi",
    "city": "Thiruvananthapuram"
  },
  "gender": "male",
  "course": "MCA",
  "mark": 60,
  "grade": "B",
  "phone": {
    "type": "land",
    "no": "04712663890"
  }
},{
  "_id": 6,
  "name": {
    "fname": "Yadu",
    "lname": "Kannan"
  },
  "address": {
    "house_name": "Sreenilayam",
    "city": "Kollam"
  },
  "gender": "male",
  "course": "Mechanical",
  "mark": 85,
  "grade": "A",
  "phone": {
    "type": "mobile",
    "no": 9446321780
  }
},{
  "_id": 7,
  "name": {
    "fname": "Vivek",
    "lname": "Bose"
  },
  "address": {
    "house_name": "Kallu",
    "city": "Ernakulam"
  },
  "gender": "male",
  "course": "MCA",
  "mark": 60,
  "grade": "B",
  "phone": {
    "type": "land",
    "no": "04842663890"
  }
},{
  "_id": 8,
  "name": {
    "fname": "Kavya",
    "lname": "Mohan"
  },
  "address": {
    "house_name": "Kavyanjali",
    "city": "Kollam"
  },
  "gender": "female",
  "course": "Mechanical",
  "mark": 95,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 9448399780
  }
},{
  "_id": 9,
  "name": {
    "fname": "Divya",
    "lname": "Vijayan"
  },
  "address": {
    "house_name": "Divyalayam",
    "city": "Varkala"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 70,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04702667890"
  }
},{
  "_id": 10,
  "name": {
    "fname": "Vimal",
    "lname": "Vinayan"
  },
  "address": {
    "house_name": "Vimala Bhavan",
    "city": "Kollam"
  },
  "gender": "male",
  "course": "Mechanical",
  "mark": 90,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 8185399780
  }
},{
  "_id": 11,
  "name": {
    "fname": "Renuka",
    "lname": "Vijayan"
  },
  "address": {
    "house_name": "Sreevilasam",
    "city": "Thiruvananthapuram"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 82,
  "grade": "A",
  "phone": {
    "type": "land",
    "no": "04712547890"
  }
},{
  "_id": 12,
  "name": {
    "fname": "Vimal",
    "lname": "Bose"
  },
  "address": {
    "house_name": "Vimalam",
    "city": "Ernakulam"
  },
  "gender": "male",
  "course": "MCA",
  "mark": 90,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 9485399780
  }
},{
  "_id": 13,
  "name": {
    "fname": "Remya",
    "lname": "V"
  },
  "address": {
    "house_name": "Sree",
    "city": "Thiruvananthapuram"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 85,
  "grade": "A",
  "phone": {
    "type": "land",
    "no": "04712647890"
  }
},{
  "_id": 14,
  "name": {
    "fname": "Vinod",
    "lname": "Paniker"
  },
  "address": {
    "house_name": "Deepam",
    "city": "Ernakulam"
  },
  "gender": "male",
  "course": "MCA",
  "mark": 70,
  "grade": "B",
  "phone": {
    "type": "mobile",
    "no": 9445399787
  }
},{
  "_id": 15,
  "name": {
    "fname": "Remya",
    "lname": "Sugunan"
  },
  "address": {
    "house_name": "Remya vilasam",
    "city": "Thiruvananthapuram"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 72,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04712648890"
  }
},{
  "_id": 16,
  "name": {
    "fname": "Jabin",
    "lname": "S"
  },
  "address": {
    "house_name": "Deepam",
    "city": "Kollam"
  },
  "gender": "male",
  "course": "Civil",
  "mark": 70,
  "grade": "B",
  "phone": {
    "type": "mobile",
    "no": 9485399787
  }
},{
  "_id": 17,
  "name": {
    "fname": "Vidhya",
    "lname": "Sugunan"
  },
  "address": {
    "house_name": "vidhya vilasam",
    "city": "Thiruvananthapuram"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 79,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04712647790"
  }
},{
  "_id": 18,
  "name": {
    "fname": "Arya",
    "lname": "Satheesh"
  },
  "address": {
    "house_name": "Arya Bhavan",
    "city": "Kollam"
  },
  "gender": "female",
  "course": "Civil",
  "mark": 90,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 9445399787
  }
},{
  "_id": 19,
  "name": {
    "fname": "Soorya",
    "lname": "S"
  },
  "address": {
    "house_name": "Meena Bhavan",
    "city": "Thiruvananthapuram"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 79,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04712647890"
  }
},{
  "_id": 20,
  "name": {
    "fname": "Amritha",
    "lname": "S"
  },
  "address": {
    "house_name": "Arya Bhavan",
    "city": "Varkala"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 99,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 9445365787
  }
},{
  "_id": 21,
  "name": {
    "fname": "Soorya",
    "lname": "P"
  },
  "address": {
    "house_name": "Soorya Bhavan",
    "city": "Thiruvananthapuram"
  },
  "gender": "female",
  "course": "MCA",
  "mark": 74,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04712641890"
  }
},{
  "_id": 22,
  "name": {
    "fname": "Arun",
    "lname": "S"
  },
  "address": {
    "house_name": "Arun Bhavan",
    "city": "Attingal"
  },
  "gender": "male",
  "course": "MCA",
  "mark": 91,
  "grade": "A+",
  "phone": {
    "type": "mobile",
    "no": 9445366987
  }
},{
  "_id": 23,
  "name": {
    "fname": "Sayooj",
    "lname": "Kiran"
  },
  "address": {
    "house_name": "Kiran Bhavan",
    "city": "Thiruvananthapuram"
  },
  "gender": "male",
  "course": "Civil",
  "mark": 74,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04712721890"
  }
},{
  "_id": 24,
  "name": {
    "fname": "Abhilash",
    "lname": "S"
  },
  "address": {
    "house_name": "Dhanya Bhavan",
    "city": "Attingal"
  },
  "gender": "male",
  "course": "Mechanical",
  "mark": 75,
  "grade": "B+",
  "phone": {
    "type": "mobile",
    "no": 8182366987
  }
},{
  "_id": 25,
  "name": {
    "fname": "Sree",
    "lname": "Raj"
  },
  "address": {
    "house_name": "Sree",
    "city": "Varkala"
  },
  "gender": "male",
  "course": "Civil",
  "mark": 74,
  "grade": "B+",
  "phone": {
    "type": "land",
    "no": "04702721890"
  }
}]

#coll.insert_many(list)

#for x in coll.find({"gender":"female","course":"MCA"}):
		#print(x["name"]["fname"]+ " " +x["name"]["lname"]+" "+x["course"]+" "+x["gender"])
#for x in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
	#print(x["name"]["fname"]+" "+x["name"]["lname"]+ " "+str(x["mark"]))
#for x in coll.find({"gender":"male","grade":"A+"}):
       	#print(x["name"]["fname"]+" "+x["name"]["lname"]+ " "+x["gender"]+" "+x["grade"])
#for x in coll.find({"course":"Mechanical"}).sort("mark",-1).limit(3):
       	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+str(x["mark"]))
#for x in coll.find({"mark":{'$gt':80,'$lt':90}}):
       	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+str(x["mark"]))
#for x in coll.find({"gender":"female","mark":{'$gt':90}}):
   	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+str(x["mark"]))
#for x in coll.find({"name.fname":{"$regex":'^V'}}):
	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+str(x["mark"]))
#for x in coll.find({"address.city":"Kollam"}):
  	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["address"]["city"])
#for x in coll.find({"address.city":{"$nin":["Thiruvananthapuram","Kollam"]}}):
       	#print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["address"]["city"])
for x in coll.find({"gender":"female","address.city":{"$in":["Thiruvananthapuram","Kollam"]}}):
	print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["address"]["city"])

	

