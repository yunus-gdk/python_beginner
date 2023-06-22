import random

a = 0
b = 10
nombre_mystere = random.randint(a, b)
nombre_essai = 5
user_choice =""

print("*** Le jeu du nombre mystère ***")

while nombre_essai > 0:

    print(f"Il te reste {nombre_essai} essai{'s.' if nombre_essai > 1 else '.'}")

    if not (user_choice.isdigit() or int(user_choice in range(a, b))):
        user_choice = input(f"Saisir un nombre entre {a} et {b}: ")
        continue
    
    print("_"*50)
    if nombre_essai == 1:
        print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
        break
    
    elif int(user_choice) == int(nombre_mystere):
        print(f"Vous avez trouvé le nombre mystère en {6 - nombre_essai} fois !")
        break
    
    elif int(user_choice) > int(nombre_mystere):
        print(f"{user_choice} est trop grand.")
        user_choice = ""
    
    elif int(user_choice) < int(nombre_mystere):
        print(f"{user_choice} est trop petit.")
        user_choice = ""
    
    nombre_essai -= 1
    