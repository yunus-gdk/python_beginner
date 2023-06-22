from random import randint

point_vie_user = point_vie_ennemi = 50
potion_user = 3

MENU = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
MENU_CHOICES = ["1", "2"]

while point_vie_user or point_vie_ennemi:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide...")
        continue

    if user_choice == "1":
        degat_attaque_user  = randint(5, 10)
        degat_attaque_ennemi = randint(5, 15)
        point_vie_user -= degat_attaque_ennemi
        point_vie_ennemi -= degat_attaque_user
        print(f"Vous avez infligé {degat_attaque_user} points de dégats à l'ennemi.")
        print(f"L'ennemi vous a infligé {degat_attaque_ennemi} points de dégats.")
        if point_vie_user > 0:
            print(f"Il vous reste {point_vie_user} points de vie.")
        else:
            print(f"Il vous reste 0 points de vie.")
        if point_vie_ennemi > 0:
            print(f"Il reste {point_vie_ennemi} points de vie à l'ennemi.")
        else:
            print(f"Il reste 0 points de vie à l'ennemi.")
    
    if user_choice == "2":
        potion_user -= 1
        if potion_user > 0:
            degat_attaque_ennemi = randint(5, 15)
            ajout_point_vie_user = randint(15, 50)
            point_vie_user += ajout_point_vie_user
            print(f"Vous récupérez {ajout_point_vie_user} points de vie ({potion_user} potions restantes.)")
            point_vie_user -= degat_attaque_ennemi
            print(f"L'ennemi vous a infligé {degat_attaque_ennemi} points de dégats.")
            if point_vie_user > 0:
                print(f"Il vous reste {point_vie_user} points de vie.")
            else:
                print(f"Il vous reste 0 points de vie.")
            print(f"Il reste {point_vie_ennemi} points de vie à l'ennemi.")
            print("-"*50)
            print("Vous passez votre tour !")
            point_vie_user -= degat_attaque_ennemi
            print(f"L'ennemi vous a infligé {degat_attaque_ennemi} points de dégats.")
            if point_vie_user > 0:
                print(f"Il vous reste {point_vie_user} points de vie.")
            else:
                print(f"Il vous reste 0 points de vie.")
            if point_vie_ennemi > 0:
                print(f"Il reste {point_vie_ennemi} points de vie à l'ennemi.")
            else:
                print(f"Il reste 0 points de vie à l'ennemi.")
        else:
            print("Vous n'avez plus de potions ...")
            continue

    if point_vie_ennemi <= 0:
        print("Tu as gagné !!!")
        print("Fin du jeu.")
        break
    elif point_vie_user <= 0:
        print("Tu as perdu !!!")
        print("Fin du jeu.")
        break    
    
    print("-"*50)