chemin = "C:/python/prenom.txt"
chemin_clean = "C:/python/prenom_clean_correction.txt"

with open(chemin, "r") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(chemin_clean, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))
