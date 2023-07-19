#!/usr/bin/env python3
""" List all documents in Python """

def list_all(mongo_collection):
    """ List all documents in a collection"""
    documents = mongo_collection.find()
    # the find method returns a cursor object which needs to be converted to a list to iterate over the documents

    if mongo_collection.count_documents({}) == 0:
        return []

    return documents

    #return mongo_collection.find()
