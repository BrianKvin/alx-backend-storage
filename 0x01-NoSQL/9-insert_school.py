#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo"""

def insert_school(mongo_collection, **kwargs):
    """ Insert a new document in a collection based on kwargs """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
