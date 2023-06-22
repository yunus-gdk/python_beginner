# # print('''test
# # 2eme ligne,
# # 3eme ligne''')

# a,b = 5,"test"
# print(a,b)

# a,b,c = 2,6,3

# resultat = str(a) + " + " + str(b) + " + " + str(c)
# print(resultat)

# # a = "J'ai une classe de " + 30 + " élèves"                    # J'ai une classe de 30 élèves
# # b = 10 + " + " + "5" + " est égal à " + 15                    # 10 + 5 est égal à 15
# # c = 10 + "5"                                                  # 15
# # d = "L'addition de 10 + 5 est égal à " + 10 + 5               # L'addition de 10 + 5 est égal à 15

# a = "J'ai une classe de " + str(30) + " élèves"          
# b = str(10) + " + " + "5" + " est égal à " + str(15)     
# c = 10 + int("5")
# d = "L'addition de 10 + 5 est égal à " + str(int(10 + 5))
# print(a,b,c,d)

# age = 20
# majeur = True if age >= 18 else False
# print(majeur)

# note = 4

# if note == 20:
#     commentaire = "C'est un sans faute !"
# elif note >= 18 and note < 20:
#     commentaire = "Excellent !!"
# elif note > 14 :
#     commentaire = "Bon travail !"
# elif note > 10 :
#     commentaire = "Peut mieux faire."
# elif note > 6 :
#     commentaire = "Il faut tout revoir..."
# elif note >= 3:
#     commentaire = "Tu n'as rien compris !"
# elif note < 3 :
#     commentaire = "Sans commentaire..."
 
# print(commentaire)

# from pathlib import Path

# p = Path.cwd()
# #p.joinpath("udemy", "testscript", "toto.py")
# p = p / "udemy" / "testscript" / "toto.py"
# # p.mkdir(parents=True, exist_ok=True)
# p.touch()
# p.write_text("bonjour")
# print(p.read_text())

# import shutil
# dossier = Path("/c/python/udemy/testscript/toto.py")
# shutil.rmtree(dossier)

def assigner_valeur():
    return 10

a = assigner_valeur()
print(a)

def afficher(message):
    print(message)

afficher("J'envoie cet argument dans le paramètre de la fonction afficher !")

def saluer(prenom):
    print("Bonjour", prenom)
 
saluer("Patrick")

def multiplicateur_mot(mot, mult=5):
	return mot * mult

mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)

class Fichier:
    nom="myfile"
    extension="pdf"
    taille=100

print(Fichier.extension)

