# GoldenMelonDB
Simple Python NoSQL Database

# Setting up
To set up GoldenMelon, simply call the class with an empty dictionary as an argument:
```
from goldendb import *

db = GoldenDB({})
```
GoldenMelon uses tables, so to create one you do:
```
db.newtable("happytable")
```
GoldenMelon is based on keys and values.
Every key __must__ be different.
Also, in GoldenMelon you can input any type of data.
To input data:
```
db.insert("happytable", "my key", ["my list of values", True, False, 12, 1.2, {"A dictionary":"in a list"}])
```
You can read data by using the get or search functions
```
db.get("happytable", "my key") //get statements search for keys in a table and returns its values. They assume you know that the key exists.
db.search("happytable", "this doesnt exist")// these look for values and returns the key-value pairs.
```
