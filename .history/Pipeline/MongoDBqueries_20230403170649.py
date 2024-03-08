from pymongo import MongoClient
from PipelineForMongoDB import *

client = MongoClient('localhost', 27017)

db = client['ngi']
existing_collection = db['cprmsCorrelationMetadata']

def find_latest_createDate(clientCode):
    # Get the collection
    mycollection = db["mycollection"]

    # Build the query
    query_filter = mycollection.find({'correlationStatus': 'SUCCESSFUL','clientCode' : getclientCodeFromUser()})
    if query_filter.count() > 0:
        return query_filter[-1]["createDate"]
    else:
        print("No data found for the given clientCode")
        return None



    # Execute the query
    result = mycollection.find(query_filter).sort

    # Return the result
    return result