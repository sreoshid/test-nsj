from pymongo import MongoClient
from PipelineForMongoDB import *

client = MongoClient('localhost', 27017)

db = client['ngi']
cprmsProperty = db['cprmsProperty']
cprmsCorrelationMetadata = db["cprmsCorrelationMetadata"]
cprmsStatisticsCorrelation = db["cprmsStatisticsCorrelation"]
cprmsAggregatedTransaction = db["cprmsAggregatedTransaction"]
cprmsBarrierGateTransaction = db["cprmsBarrierGateTransaction"]
skiDataEntryExit = db["skiDataEntryExit"]
skiDataRevenueTicket = db["skiDataRevenueTicket"]
advamReservation = db["advamReservation"]


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
    
def getStatCorrelationId(code, latest_create_date, rollback_date):
    query_filter =  cprmsCorrelationMetadata.find({'clientCode' : code, '_id' : {"$exists": True}, 
                                        'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    # results = cprmsProperty.find(query_filter)
    correlation_metadata_id = []

    for document in query_filter:
        correlation_metadata_id = document.get('_id')
        correlation_metadata_id = correlation_metadata_id.append(correlation_metadata_id)
        return correlation_metadata_id
    
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

def getStatCorrelationId(code, latest_create_date, rollback_date):
    query_filter =  cprmsStatisticsCorrelation.find({'clientCode' : code, '_id' : {"$exists": True}, 
                                        'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    statestics_corr_id = []

    for document in query_filter:
        statestics_corr_id = document.get('_id')
        statestics_corr_id = statestics_corr_id.append(statestics_corr_id)
        return statestics_corr_id

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
    statCorrltn_unprcsd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'UNPROCESSED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_unprcsd_count

def statCorrltnFaildStatus(code, latest_create_date, rollback_date):
    statCorrltn_faild_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'FAILED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_faild_count

def statCorrltnDplctStatus(code, latest_create_date, rollback_date):
    statCorrltn_dplct_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'DUPLICATE', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_dplct_count

def statCorrltnDltdStatus(code, latest_create_date, rollback_date):
    statCorrltn_dltd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'DELETED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_dltd_count

def statCorrltnToBeDltdStatus(code, latest_create_date, rollback_date):
    statCorrltn_tobe_dltd_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'TOBEDELETED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_tobe_dltd_count

def statCorrltnErrorStatus(code, latest_create_date, rollback_date):
    statCorrltn_error_count = cprmsStatisticsCorrelation.count_documents({'clientCode' : code, 'status' : 'ERROR', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': latest_create_date}})
    return statCorrltn_error_count

def getTransformedTxnsCount(code, rollback_date):
    skidata_entry_exit_state_count = []
    transformed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'TRANSFORMED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    accepted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ACCEPTED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    ignored_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'IGNORED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    pending_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'PENDING', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    rejected_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'REJECTED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    unprocessed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'UNPROCESSED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    failed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'FAILED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    duplicate_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'DUPLICATE', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    deleted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'DELETED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    to_be_deleted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'TOBEDELETED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    error_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ERROR', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_entry_exit_state_count.append(transformed_state_count,accepted_state_count,ignored_state_count,
                                                 pending_state_count,rejected_state_count,unprocessed_state_count,
                                                 failed_state_count,duplicate_state_count,deleted_state_count,)

def getAccptedTxnsCount(code, rollback_date):
    accepted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ACCEPTED', 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return accepted_state_count

def 
    











    
    




    # Execute the query
    # result = mycollection.find(query_filter).sort

    # Return the result
    # return result