# Simple NoSQL Python Database

class GoldenDB():
    def __init__(self, database):
        
        # Create a dictionary for database
        self.database = database
    
    def insert(self, key, value):
        # Add key-value pair
        self.database.update({key:value})
    
    def get(self, key):
        container = self.database.get(key, None)
        return container
    
    def delete(self, key):
        # delete key value pairs
        del self.database[key]
    
    def save(self, filename):
        import json
        # save contents of database in JSON
        with open(filename, "w") as fh:
            json.dump(self.database, fh)

    def load(self, filename):
        import json
        # load contents of JSON into database
        with open(filename, "r") as fh:
            self.database = json.load(fh)
    
    def listall(self):
        return self.database.items()
    
    def search(self, query):
        if query in self.database:
            return self.database[query]
        else:
            return "Not in database"
