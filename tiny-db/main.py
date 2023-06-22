from tinydb import TinyDB
# from tinydb.storages import MemoryStorage

db = TinyDB('data.json', indent=4)
# db.insert({"name": "Patrick", "score": 0})
db.insert_multiple([
    {"name": "Maxime", "score": 70},
    {"name": "René", "score": 90}
])