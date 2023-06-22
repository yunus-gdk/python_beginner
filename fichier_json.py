import json
import os

chemin = "C:/python/fichier.json"
# with open(chemin, "w") as f:
with open(chemin, "r") as f:
    # json.dump("Bonjour", f)
    # json.dump(list(range(10)), f, indent=4)
    liste = json.load(f)
    print(liste)

print(os.path.dirname(__file__))