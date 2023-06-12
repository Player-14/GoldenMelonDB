# Simple NoSQL Python Database

class GoldenDB():
    def __init__(database):
        import json
        database = {}
    
    def insert(key, value):
        database.append[key] = value
    
    def get(key):
        container = database.get(key, None)
        return container
    
    def delete(key):
        # delete key value pairs
        del database[key]

