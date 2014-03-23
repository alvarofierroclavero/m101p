# Check value before removing orphan images.
# Remove orphan images.

import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.photos

def findOrphans():

    print "Executing f7.7"

    try:
    	# Retrieve the image albums from the database.
    	albumsCursor = db.albums.find({}).sort('_id')
    	# Create an array to hold the list of all image IDs which are associated with an image album.
    	imagesArray = []

    	# Loop the query result and pull out all the image IDs part of each album. Create an array which holds
    	# all the image IDs from ALL albums so it can be easily sorted and searched later.
    	print 'Building valid images array...'
    	sanity = 0
    	for doc in albumsCursor:
    		sanity = sanity + 1
    		#print 'Working on album:', doc['_id']
    		for imageID in doc['images']:
    			if imageID not in imagesArray:
    				# image ID is not in the array, add it
    				imagesArray += [imageID]
    			else:
    				print int(imageID), 'is already in array, skipping'
    		#if sanity == 2:
    		#	break

    	print 'imagesArray:', len(imagesArray)

        # Retrieve the images from the database.
        imagesCursor = db.images.find({}).sort('_id')
        # Create an array of image IDs which need to be deleted from the database.
        imagesToDel = []

        # Loop the query (image documents) and determine whether each document is an orphan (not in an album).
        print 'Starting image search...'
        for doc in imagesCursor:
        	# Check the image ID and see if it is present in the imagesArray. If not, this image needs to be deleted from the
        	# database.
        	if doc['_id'] not in imagesArray:
        		imagesToDel += [doc['_id']]

        print 'imagesToDel:', len(imagesToDel)

        # Delete the orphan image documents from the database.
        print 'Starting image deletion...'
        sanity = 0
        for image in imagesToDel:
        	sanity = sanity + 1
        	#print 'deleting image:', image
        	removedImageCursor = db.images.remove({'_id':image})

		#if sanity == 2:
		#	break

        print 'Done!'

    except:
        print "Unexpected error:", sys.exc_info()[0]

findOrphans()
