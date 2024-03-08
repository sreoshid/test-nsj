from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from datetime import datetime
from MongoDBqueries import *

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)


def getclientCodeFromUser():
    #   clientCode = ""
      while True:
        clientCode = str(input("Enter the Location/Client Code: "))
        if (clientCode in ['RDU', 'LGA', 'EWR', 'JFK', 'ZRH', 'LHR', 'PHX']):
            break
      return clientCode

print (getclientCodeFromUser())


         
rollback_date = input("Enter a date in YYYY-MM-DD format: ")
try:
    date = datetime.strptime(rollback_date, "%Y-%m-%d")
    today = datetime.today()
    if date < today:
        print("The input date is less than today's date.")
    else:
        print("The input date is not less than today's date.")
except ValueError:
    print("Invalid date format!")

# Select the database and collection
db = client['ngi']
existing_collection = db['cprmsCorrelationMetadata']

# Define the pipeline stages
pipeline = [
    {'$match': {'correlationStatus': 'SUCCESSFUL','clientCode' : 'RDU'}}
    # { '$addFields': { 'new_id': '$_id' } },
    # { '$project': { '_id': 0, 'createDate': 1, 'additionalInformation': 1 } },
]

# Aggregate the data and insert it into the new collection
data = list(existing_collection.aggregate(pipeline))
#db.collection_name.aggregate(aggregate operations)

new_db = client['test']
new_collection = new_db['cprmsCorrelationMetaDataTemp']
new_collection.delete_many({})
    
try:
        result = new_collection.insert_many(data)


finally:
        client.close()
# Rename the _id field in the new collection
# new_collection.update_many({}, {'$rename': {'_id': 'cprmsCorrelationMetaDataId'}})
# Close the database connection


