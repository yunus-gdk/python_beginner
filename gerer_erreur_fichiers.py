fichier = input("Spécifiez le chemin complet du fichier à ouvrir: ")

try:
	with open(fichier, "r", encoding='utf-8') as f:
		contenu = f.read()
		print(contenu)
except FileNotFoundError as e:
	print("Erreur: ", e)
except UnicodeDecodeError as e:
    print("Erreur: ", e)
else:
	f.close()
# finally:
# 	print("ok")
	