#!/usr/bin/env python3
""" MongoDB with Python using pymongo"""

def top_students(mongo_collection):
    """Returns all students sorted by average """
    lead_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
            },
        {"$sort": {"averageScore": -1}}
        ])
    return lead_student
