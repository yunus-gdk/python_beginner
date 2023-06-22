from tinydb import TinyDB, Query, where

db = TinyDB('data.json', indent=4)

User = Query()
patrick = db.search(User.name == "Patrick")
print(patrick)

remi_unique = db.get(User.name == "Remi")
print(remi_unique)

high_scores = db.search(where("score") > 0)
print(high_scores)

print(f"Nombre d'elements dans la DB {len(db)}")

print(db.contains(User.name == "Patrick")) # return True or False
print(db.count(User.name == "Patrick"))