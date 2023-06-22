from pprint import pprint

new_list = []
chemin = "C:/python/prenom.txt"
chemin_clean = "C:/python/prenom_clean.txt"
with open(chemin, "r", encoding='utf-8') as f:
    contenu = f.read().splitlines()
    
for line in contenu:
    new_list.extend(line.split())     # splits a string into a list     # extend() method adds all the elements to the end of the list

prenoms_finaux = [prenom.strip(" .,") for prenom in new_list]           # removes any spaces characters
prenoms_finaux.sort()

with open(chemin_clean, "w", encoding='utf-8') as f:
    for item in prenoms_finaux:           
        f.write("%s\n" % item)        # write each item on a new line