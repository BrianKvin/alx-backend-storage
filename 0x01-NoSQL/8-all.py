#!/usr/bin/env python3
""" List all documents in Python """

def list_all(mongo_collection):
    """ List all documents in a collection"""
    #documents = list(mongo_collection.find())


    #if len(documents) == 0:
    #    return []

    #return documents

    return mongo_collection.find()
