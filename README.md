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
