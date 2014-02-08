import pymongo
import bottle
import sys

@bottle.get("/sc/<db_name>")
def show_collections(db_name):
	try:
		# Setup connection to the local mongod server
		connection = pymongo.MongoClient("mongodb://localhost")
		
		# Setup error controls.
		error_val = 0
		error_message = ""

		# Attempt to attach a Mongo connection to the requested database.

		db = connection[db_name]

		# Attempt to retrieve a listing of all the collections in the preferred database.
		collections = db.collection_names()

		# If the collections exist, print them in the HTML template. If they don't exist show an error.
		if len(collections) == 0:
			error_val = 1
			error_message = "Invalid database requested."
		
		return bottle.template('show_collections', {'error_val':error_val, 'error_message':error_message, 'db_name':db_name, 'collections':collections})
	except:
		error_val = 1
		error_message = sys.exc_info()[0]
		return bottle.template('show_collections', {'error_val':error_val, 'error_message':error_message, 'db_name':db_name})

bottle.debug(True)
bottle.run(host='localhost', port=8080)