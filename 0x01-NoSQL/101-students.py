#!/usr/bin/env python3
'''Task 14's module.
'''

def top_students(mongo_collection):
    '''
    Prints all students in a collection sorted by average score.
    '''
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': {'$avg': '$topics.score'}},
                'topics': 1,
            },
        },
        {
            '$sort': {'averageScore': -1},
        },
    ]

    students = mongo_collection.aggregate(pipeline)
    return students

