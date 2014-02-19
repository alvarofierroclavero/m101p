
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
students = db.students

def find():

    print "Executing hw3.1"

    try:
        # students.aggregate([{'$unwind':'$scores'}, {'$match': {'scores.type': 'homework'}}, {'$sort': {'scores.score':1}}, {'$limit': 2}])

        # 0. initial query I tried:
        # results = students.aggregate([{'$unwind':'$scores'}, {'$match': {'scores.type': 'homework'}}, {'$sort': {'scores.score':1}}])

        # 1. find the lowest score w/o respect to score type
        # results = students.aggregate( [ { '$unwind': '$scores' }, {'$group': { '_id':'$_id' , 'minscore': {'$min': '$scores.score' } } } ] )

        # 2. find the lowest homework score
        results = students.aggregate( [ { '$unwind': '$scores' }, {'$match': {'scores.type': 'homework'}}, {'$group': { '_id':'$_id' , 'minscore': {'$min': '$scores.score' } } } ] )

    except:
        print "Unexpected error:", sys.exc_info()[0]

    #print "Results: " + str(results['result'])

    counter = 0
    if results['result']:
    	for doc in results['result']:
    		counter = counter + 1
    		print counter
    		print doc['_id']
    		print doc['minscore']
    		print '--------------'
    		students.update( { '_id': doc['_id'] }, { '$pull': { 'scores': { 'score': doc['minscore'] } } } )

find()