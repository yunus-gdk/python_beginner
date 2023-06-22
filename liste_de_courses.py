liste_course = []
choix_menu = ["1", "2", "3", "4", "5"]

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

while True:
    print("_"*50)
    choix = input(MENU)

    print("\n")
    if choix not in choix_menu:
        print("Veuillez choisir une option valide: 1, 2, 3, 4 ou 5")
        continue

    if choix == "1":
        element = input("Entrer le nom d'un élèment à ajouter à la liste de courses: ")
        liste_course.append(element)
        print("\n")
        print("_"*50)
        print(f"L'élèment {liste_course[-1]} a été ajouté à la liste.")
        
    elif choix == "2":
        if len(liste_course) == 0:
            print("La liste est déjà vide !!!")
        else:
            element = input("Entrer le nom d'un élèment à retirer de la liste de courses: ")
            if element in liste_course:
                liste_course.remove(element)
                print(f"L'élèment {element} a bien été supprimé de la liste.")
            else: 
                print(f"L'élèment {element} n'est pas dans la liste.")
        
    elif choix == "3":
        if liste_course:
            print(f"Voici le contenu de votre liste : ")
            for i, element in enumerate(liste_course, 1):
                print(f"{i}. {element}")
        else:
            print("Votre liste ne contient aucun élèment.")
        
    elif choix == "4":
        if liste_course:
           liste_course.clear()
           print("La liste a été vidée de son contenu !")
        else:
            print("La liste est déjà vide !!!")
        
    elif choix == "5":
        print("A bientôt !!!")
        break
