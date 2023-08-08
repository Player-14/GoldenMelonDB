# GoldenMelonDB NoSQL Python Database

class GoldenDB():
    def __init__(self, database):
        # Create a dictionary for database
        self.database = {}

    def newtable(self, table):
        # Create nested dictionary as table
        self.database.update({table:{}})

    def anewtable(self, table):
        if table not in self.database:
            self.database.update({table:{}})
        else:
            return self.listall(table)

    def insert(self, table, key, value):
        # Add key-value pairs
        self.database[table].update({key:value})
    
    def get(self, table, key):
        # gets the value for a particular key
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
            return f"File {filename} Not Found!"
    
    def loade(self, filename):
        import ujson
        try: # attempt to load database
            with open(filename, "r") as fh:
                self.database = ujson.load(fh)
        except FileNotFoundError: # if file not found, make new file
            open(filename, "w")
        except ujson.JSONDecodeError:
            return f"Empty Contents"

    def listall(self, table):
        # list all contents of database
        return list(self.database[table].items())

    def wipe(self, table):
        # overwrite existing database file with empty dictionary
        if table is None:
            self.database = {}
        else:
            self.database[table] = {}
    
    def search(self, table, query):
        # searches a table in the database for a specific key/value
        if query in self.database:
            return self.database[table][query]
        else:
            return "Not in database"

    def uninsert(self):
        # removes the last inserted object
        self.database[table].popitem()

    def countdb(self, table):
        # count the amount of items in the database
        return len(self.database[table].keys())

    def ininsert(self, table, key, value):
        # inserts data if data doesn't exist
        return self.database[table].setdefault(key, value)

    def tables(self):
        # returns a list of all of the tables
        return self.database.keys()
    
