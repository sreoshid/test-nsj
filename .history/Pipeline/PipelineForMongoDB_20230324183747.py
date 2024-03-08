from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Select the database and collection
db = client['ngi']
existing_collection = db['cprmsCorrelationMetadata']

# Define the pipeline stages
pipeline = [
    { '$match': { 'correlationStatus': 'SUCCESSFUL' } },
    { '$project': { '_id': 0} },
]

# Aggregate the data and insert it into the new collection
data = list(existing_collection.aggregate(pipeline))

new_db = client['test']
new_collection = new_db['cprmsCorrelationMetaDataTemp']

result = new_collection.insert_many(data)

# Rename the _id field in the new collection
# new_collection.update_many({}, {'$rename': {'_id': 'cprmsCorrelationMetaDataId'}})

# Close the database connection
client.close()