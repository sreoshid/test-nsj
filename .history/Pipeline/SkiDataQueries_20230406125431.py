from pymongo import MongoClient
from PipelineForMongoDB import *
from MongoDBqueries import *
import PipelineForMongoDB

client = MongoClient('localhost', 27017)

db = client['ngi']
skiDataRevenueTicket = db["skiDataRevenueTicket"]

code = PipelineForMongoDB.getclientCodeFromUser()


def getSkiEntryExtAccptedTxnsCount(code, rollback_date, correlation_metadata_id):
    accepted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ACCEPTED', 
                                                             'correlationMetadataId' : {'$in': MongoDBqueries.correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return accepted_state_count

def getSkiEntryExtIgnrdTxnsCount(code, rollback_date, correlation_metadata_id):
    ignored_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'IGNORED', 
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return ignored_state_count

def getSkiEntryExtPndngTxnsCount(code, rollback_date, correlation_metadata_id):
    pending_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'PENDING', 
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return pending_state_count

def getSkiEntryExtRjctdTxnsCount(code, rollback_date, correlation_metadata_id):
    rejected_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'REJECTED', 
                                                             'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return rejected_state_count

def getSkiEntryExtUnprcsdTxnsCount(code, rollback_date, correlation_metadata_id):
    unprocessed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'UNPROCESSED',
                                                                'correlationMetadataId' : {'$in': correlation_metadata_id}, 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return unprocessed_state_count

def getSkiEntryExtFaildTxnsCount(code, rollback_date, correlation_metadata_id):
    failed_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'FAILED', 
                                                           'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return failed_state_count

def getSkiEntryExtDuplctTxnsCount(code, rollback_date, correlation_metadata_id):
    duplicate_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'DUPLICATE', 
                                                              'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return duplicate_state_count

def getSkiEntryExtDeletedTxnsCount(code, rollback_date, correlation_metadata_id):
    deleted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'DELETED',
                                                            'correlationMetadataId' : {'$in': correlation_metadata_id}, 
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return deleted_state_count

def getSkiEntryExtToBeDeletedTxnsCount(code, rollback_date, correlation_metadata_id):
    to_be_deleted_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'TOBEDELETED', 
                                                                  'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return to_be_deleted_state_count

def getSkiEntryExtErrorTxnsCount(code, rollback_date, correlation_metadata_id):
    error_state_count = skiDataEntryExit.count_documents({'clientCode' : code, 'status' : 'ERROR', 
                                                          'correlationMetadataId' : {'$in': correlation_metadata_id},
                                                  'createDate' : {'$gte': rollback_date,'$lte': rollback_date}})
    return error_state_count