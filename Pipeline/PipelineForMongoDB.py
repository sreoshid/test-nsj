from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from datetime import datetime
import MongoDBqueries
import sys 
import os
import SkiDataQueries

sys.path.append(os.path.abspath("C:\Users\srdasg\python\Pipeline"))
client = MongoClient('localhost', 27017)
code = ""
latestCreateDate = MongoDBqueries.find_latest_createDate(code)
oldestCreateDate = MongoDBqueries.find_oldest_createDate(code)

def getclientCodeFromUser():
      while True:
        clientCode = str(input("Enter the Location/Client Code: ")).upper()
        if (clientCode in ['RDU', 'LGA', 'EWR', 'JFK', 'ZRH', 'LHR', 'PHX']):
            break
      code = clientCode  
      return code

def getRollbackDateFromUser(oldestCreateDate,latestCreateDate):
    rollback_date = input("Enter a date in YYYY-MM-DD format: ")
    try:
        rollback_date = datetime.strptime(rollback_date, "%Y-%m-%d")
        
        if latestCreateDate == None:
         raise ValueError
        if oldestCreateDate <= rollback_date <= latestCreateDate:
            return rollback_date
        else:
            print("No data is present for the entered date.")
    except ValueError:
        print("Invalid date format!")

def getTranformedToAcceptedFileCount()














# Select the database and collection
# db = client['ngi']
# existing_collection = db['cprmsCorrelationMetadata']

# Define the pipeline stages
# pipeline = [
#     {'$match': {'correlationStatus': 'SUCCESSFUL','clientCode' : 'RDU'}}
#     { '$addFields': { 'new_id': '$_id' } },
#     { '$project': { '_id': 0, 'createDate': 1, 'additionalInformation': 1 } }
# ]

# Aggregate the data and insert it into the new collection
# data = list(existing_collection.aggregate(pipeline))
#db.collection_name.aggregate(aggregate operations)

# new_db = client['test']
# new_collection = new_db['cprmsCorrelationMetaDataTemp']
# new_collection.delete_many({})
    
# try:
#         result = new_collection.insert_many(data)


# finally:
#         client.close()
# Rename the _id field in the new collection
# new_collection.update_many({}, {'$rename': {'_id': 'cprmsCorrelationMetaDataId'}})
# Close the database connection


