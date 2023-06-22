films = {
    1: {
        "nom": "Le Seigneur des Anneaux",
        "prix": 12
    },
    2: {
        "nom": "Harry Potter",
        "prix": 9
    },
    3: {
        "nom": "Blade Runner",
        "prix": 7.5
    }
}
prix = 0

# for key in films:
#     print(key)

for value in films.values():
    # print(value)
    prix += value.get("prix")
print(prix)
    

films1 = {
    "Le Seigneur des Anneaux": 12,
    "Harry Potter" : 9,
    "Blade Runner": 7.5
}
prix1 = 0

print(films1['Harry Potter'])

for value in films1.values():
    prix1 += value
for key in films1:
    print(films1[key])

print(prix1)
