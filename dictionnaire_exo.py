employes = {
    "id01": 
        {
            "prenom": "Paul", 
            "nom": "Dupont", 
            "age": 32},
    "id02": 
        {
            "prenom": "Julie", 
            "nom": "Dupuit", 
            "age": 25},
    "id03": 
        {
            "prenom": "Patrick", 
            "nom": "Ferrand", 
            "age": 36}
}

# Patrick a quitté l'entreprise cette année, nous devons donc l'enlever du dictionnaire.
# Julie a fêté son anniversaire hier, il faut donc changer son âge (elle a maintenant 26 ans).
# Paul quant à lui fêtera son anniversaire la semaine prochaine. Nous voulons donc récupérer son âge pour savoir quel âge il aura.

employes.pop("id03")
print(employes)

print(employes["id02"]["age"])
employes["id02"]["age"]=26
print(employes["id02"]["age"])

print(employes["id01"].get("age"))