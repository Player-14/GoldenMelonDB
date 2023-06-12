# Simple NoSQL Python Database

class GoldenDB():
    def __init__(database):
        import json
        # Create a dictionary for database
        database = {}
    
    def insert(key, value):
        # Add key-value
        database.append[key] = value
    
    def get(key):
        container = database.get(key, None)
        return container
    
    def delete(key):
        # delete key value pairs
        del database[key]
    
    def save(filename):
        # save contents of database in JSON
        with open(filename, "w") as fh:
            json.dump(database, fp)

    def load(filename):
        # load contents of JSON into database
        with open(filename, "r") as fh:
            database = json.load(fp)
    
    def listall():
        return list(database)
    
    def search(query):
        if query in database:
            return database[query]
        else:
            return "Not in database"
    
        
