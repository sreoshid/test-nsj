from pymongo import MongoClient
from PipelineForMongoDB import *
import MongoDBqueries
import PipelineForMongoDB

client = MongoClient('localhost', 27017)

db = client['ngi']
skiDataEntryExit = db["skiDataEntryExit"]
skiDataRevenueTicket = db["skiDataRevenueTicket"]

code = PipelineForMongoDB.getclientCodeFromUser()
latest_create_date = MongoDBqueries.find_latest_createDate(code)
rollback_date = PipelineForMongoDB.getRollbackDateFromUser(code)
correlation_metadata_id = MongoDBqueries.getCorrelatnMetaDataId(code, latest_create_date, rollback_date)


def getSkiEntryExtAccptedTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_accepted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ACCEPTED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_accepted_state_count

def getSkiEntryExtTrnsfrmdTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_transformed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'TRANSFORMED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$lte': {'$date' : rollback_date}},
                                                  'lastModifiedDate':{'$gte': rollback_date}})
    return skidata_transformed_state_count

def getSkiEntryExtIgnrdTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_ignored_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'IGNORED', 
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_ignored_state_count

def getSkiEntryExtPndngTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_pending_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'PENDING', 
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_pending_state_count

def getSkiEntryExtRjctdTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_rejected_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'REJECTED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_rejected_state_count

def getSkiEntryExtUnprcsdTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_unprocessed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'UNPROCESSED',
                                                                'correlationMetadataId' : {'$in': correlation_metadata_id}, 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_unprocessed_state_count

def getSkiEntryExtFaildTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_failed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'FAILED', 
                                                           'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_failed_state_count

def getSkiEntryExtDuplctTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_duplicate_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'DUPLICATE', 
                                                              'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_duplicate_state_count

def getSkiEntryExtDeletedTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_deleted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'DELETED',
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id}, 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_deleted_state_count

def getSkiEntryExtToBeDeletedTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_to_be_deleted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'TOBEDELETED', 
                                                                  'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_to_be_deleted_state_count

def getSkiEntryExtErrorTxnsCount(code, rollback_date, correlation_metadata_id):
    skidata_error_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ERROR', 
                                                          'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return skidata_error_state_count

# SKIDATA Revenue status query

def getSkiDataRevErrorTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_error_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'ERROR', 
                                                          'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_error_state_count

def getSkiDataRevAccptedTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_accepted_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'ACCEPTED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_accepted_state_count

def getSkiDataRevTrnsfrmdTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_transformed_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'TRANSFORMED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_transformed_state_count

def getSkiDataRevIgnrdTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_ignored_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'IGNORED', 
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_ignored_state_count

def getSkiDataRevPndngTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_pending_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'PENDING', 
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_pending_state_count

def getSkiDataRevRjctdTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_rejected_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'REJECTED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_rejected_state_count

def getSkiDataRevUnprcsdTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_unprocessed_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'UNPROCESSED',
                                                                'correlationMetadataId' : {'$in': correlation_metadata_id}, 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_unprocessed_state_count

def getSkiDataRevFaildTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_failed_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'FAILED', 
                                                           'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_failed_state_count

def getSkiDataRevDuplctTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_duplicate_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'DUPLICATE', 
                                                              'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_duplicate_state_count

def getSkiDataRevDeletedTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_deleted_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'DELETED',
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id}, 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_deleted_state_count

def getSkiDataRevToBeDeletedTxnsCount(code, rollback_date, correlation_metadata_id):
    rev_to_be_deleted_state_count = skiDataRevenueTicket.count_documents({'clientCode' : code, 'status' : 'TOBEDELETED', 
                                                                  'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rev_to_be_deleted_state_count