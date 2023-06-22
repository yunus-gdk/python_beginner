from tinydb import TinyDB, Query, where

db = TinyDB("data.json", indent=4)

db.update({"score": 10}, where ("name") == "Patrick")
db.update({"roles": ["Junior"]})
db.update({"roles": ["Expert"]}, where("name") == "Patrick")

db.upsert({"name": "Pierre", "score": 120, "roles": ["Senior"]}, where("name") == "Pierre")

db.remove(where("score") == 0)

# db.truncate() # supprime tout le contenu de la db