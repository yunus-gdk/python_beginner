a = 5
b = "0"
try:
	resultat = a / b
except ZeroDivisionError:
	print("Division par zero impossible.")
except TypeError as e:
	print("Erreur: ", e)
except NameError as e:
	print("Erreur: ", e)
else:
	print(resultat)
finally:
	print("xxxxxxxxxxxxxxxxx")