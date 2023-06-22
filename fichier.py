chemin = "C:/python/fichier.txt"
with open(chemin, "r", encoding='utf-8') as f:
                    # w = write => remplace
                    # a = append => ajoute
    # contenu = f.read()
    # contenu = repr(f.read())
    # contenu = f.readlines()
    contenu = f.read().splitlines()
    print(contenu)
