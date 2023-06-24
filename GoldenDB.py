# Simple NoSQL Python Database

class GoldenDB():
    def __init__(self, database):
        # Create a dictionary for database
        self.database = {}

    def newtable(self, table):
        self.database.update({table:{}})

    def insert(self, table, key, value):
        # Add key-value pairs
        self.database[table].update({key:value})
    
    def get(self, table, key):
        container = self.database[table].get(key, None)
        return container
    
    def delete(self, table, key):
        # delete key value pairs
        del self.database[table][key]
    
    def save(self, filename):
        import ujson
        # save contents of database in JSON
        with open(filename, "w") as fh:
            ujson.dump(self.database, fh)

    def load(self, filename):
        import ujson
        # load contents of JSON into database
        try:
            with open(filename, "r") as fh:
                self.database = ujson.load(fh)
        except FileNotFoundError:
            return "File {filename} Not Found!"
    
    def listall(self, table):
        # list all contents of database
        return self.database[table].items()

    def wipe(self, table):
        # overwrite existing database file with empty dictionary
        if table is None:
            self.database = {}
        else:
            self.database[table] = {}
    
    def search(self, table, query):
        if query in self.database:
            return self.database[table][query]
        else:
            return "Not in database"
    def uninsert(self):
        # remove last inserted object
        self.database[table].popitem()

    def countdb(self, table):
        return len(self.database[table].items())

    def ininsert(self, table, key, value):
        return self.database[table].setdefault(key, value)

    def tables(self):
        return self.database.keys()
    
