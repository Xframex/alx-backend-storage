#!/usr/bin/env python3
'''Task 9
'''


def insert_school(mongo_collection, **kwargs):
    '''Insert  new document
    '''
    mongo_obj = mongo_collection.insert_one(kwargs)
    return mongo_obj.inserted_id
