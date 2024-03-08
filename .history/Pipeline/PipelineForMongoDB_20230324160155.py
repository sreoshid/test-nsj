from pymongo import MongoClient



# Connect to the MongoDB server
client = MongoClient('localhost', 27017)



# Select the database and collection
db_ngi = client['ngi']
db_test = client['test']
existing_collection = db_ngi['cprmsCorrelationMetaData']
new_collection = db_test['cprmsCorrelationMetaDataTemp']



# Define the pipeline stages
pipeline = [
  { '$match': { 'correlationStatus': 'SUCCESSFUL' } },
  #{ '$project': { '_id': 0, 'field1': 1, 'field2': 1 } },
  { '$out': 'cprmsCorrelationMetaDataTemp' }
]



# Execute the pipeline and create the new collection
existing_collection.aggregate(pipeline)



# Close the database connection
client.close()