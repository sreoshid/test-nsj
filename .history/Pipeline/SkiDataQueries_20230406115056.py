from pymongo import MongoClient
from PipelineForMongoDB import *

client = MongoClient('localhost', 27017)

db = client['ngi']
skiDataRevenueTicket = db["skiDataRevenueTicket"]