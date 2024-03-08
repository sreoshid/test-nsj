from pymongo import MongoClient
from PipelineForMongoDB import *

client = MongoClient('localhost', 27017)

db = client['ngi']
cprmsProperty = db['cprmsProperty']
cprmsCorrelationMetadata = db["cprmsCorrelationMetadata"]
cprmsStatisticsCorrelation = db["cprmsStatisticsCorrelation"]

def find_latest_createDate(code):
    query_filter = cprmsCorrelationMetadata.find({'clientCode' : code})
    if query_filter.count() > 0:
        latest_create_date =  query_filter[-1]["createDate"]
        return latest_create_date
    else:
        print("No data found for the given clientCode")
        return None
    
def find_oldest_createDate(code):

    # Build the query
    query_filter = cprmsCorrelationMetadata.find({'clientCode' : code})
    if query_filter.count() > 0:
        oldest_create_date =  query_filter[0]["createDate"]
        return oldest_create_date
    else:
        print("No data found for the given clientCode")
        return None
    
def getCprmsPropertyForClientCode(code):
    query_filter =  cprmsProperty.find({'clientCode' : code, 'propertyCode' : {"$exists": True}})
    # results = cprmsProperty.find(query_filter)
    carpark = []

    for document in query_filter:
        carpark = document.get('propertyCode')
        carpark = carpark.append(carpark)
        return carpark
    
def metaDataSuccessfulCountStatus(code,latest_create_date, rollback_date):
    meta_suc_count = cprmsCorrelationMetadata.count_documents({'clientCode' : code, 'correlationStatus' : 'SUCCESSFUL', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    
    return meta_suc_count

def metaDataQueueCountStatus(code, latest_create_date, rollback_date):
    meta_que_count = cprmsCorrelationMetadata.count_documents({'clientCode' : code, 'correlationStatus' : 'QUEUED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    
    return meta_que_count

def metaDataFailCountStatus(code, latest_create_date, rollback_date):
    meta_fail_count = cprmsCorrelationMetadata.count_documents({'clientCode' : code, 'correlationStatus' : 'FAILED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return meta_fail_count
    
def metaDataAbndCountStatus(code, latest_create_date, rollback_date):
    meta_abnd_count = cprmsCorrelationMetadata.count_documents({'clientCode' : code, 'correlationStatus' : 'ABANDONED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return meta_abnd_count
    
def metaDataIprCountStatus(code, latest_create_date, rollback_date):
    meta_ipr_count = cprmsCorrelationMetadata.count_documents({'clientCode' : code, 'correlationStatus' : 'In Progress', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return meta_ipr_count

def statCorrltnAccptdStatus(code, latest_create_date, rollback_date):
    statCorrltn_accptd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'ACCEPTED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_accptd_count

def statCorrltnIgnrdStatus(code, latest_create_date, rollback_date):
    statCorrltn_ignrd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'IGNORED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_ignrd_count

def statCorrltnPndngStatus(code, latest_create_date, rollback_date):
    statCorrltn_pndng_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'PENDING', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_pndng_count

def statCorrltnRjctdStatus(code, latest_create_date, rollback_date):
    statCorrltn_rjctd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'REJECTED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_rjctd_count

def statCorrltnTrnsfmdStatus(code, latest_create_date, rollback_date):
    statCorrltn_trnsfmd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'TRANSFORMED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_trnsfmd_count

def statCorrltnUnprcsdStatus(code, latest_create_date, rollback_date):
    statCorrltn_Unprcsd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'UNPROCESSED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_trnsfmd_count








    
    




    # Execute the query
    # result = mycollection.find(query_filter).sort

    # Return the result
    # return result