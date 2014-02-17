
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
grades = db.grades


def find():

    print "Executing hw2.2"

    try:
        # db.grades.find({'type':'homework'}).sort({'student_id':1, 'score':1})
        cursor = db.grades.find({'type':'homework'})
        cursor = cursor.sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    studentID = -1
    for doc in cursor:
        if studentID != doc['student_id']:
        	print "DELETE Object ID: " + str(doc['_id']) + " Score: " + str(doc['score'])
        	db.grades.remove({'_id':doc['_id']})
        	#print delDoc
        else:
        	print "KEEP Object ID: " + str(doc['_id']) + " Score: " + str(doc['score'])
        studentID = doc['student_id']
        objectID = doc['_id']
        #currentScore = doc['score']
        #print "ID: " + str(studentID) + " Score: " + str(currentScore)

find()