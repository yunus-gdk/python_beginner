import json

chemin = "C:/python/fichier-ajout.json"

# with open(chemin, "w") as f:
#     json.dump(list(range(10)), f, indent=4)

with open(chemin, "r") as f:
    liste = json.load(f)

liste.append(10)

with open(chemin, "w") as f:
    json.dump(liste, f, indent=4)
    # json.dump("Pèche", f, ensure_ascii=False)