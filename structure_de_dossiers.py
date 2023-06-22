from pathlib import Path
chemin = Path.cwd() / "dossiers"

d = {
    "Films": ["Le seigneur des anneaux","Harry Potter","Moon","Forrest Gump"],
    "Employes": ["Paul","Pierre","Marie"],
    "Exercices": ["les_variables","les_fichiers","les_boucles"]
}

for key in d.keys():
    output_dir = chemin / key
    for i in d[key]:
        output_dir_complet = output_dir / i
        output_dir_complet.mkdir(parents=True, exist_ok=True)
