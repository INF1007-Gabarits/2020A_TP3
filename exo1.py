# TODO
def lireFichier():
    chemin = "./"
    nom = "listeDeNombres.txt"

    # Ouvrir le fichier en mode de lecture à l'aide d'un context manager
    with open(chemin + nom, 'r') as f:
        #Lire les lignes du fichier dans une liste de lignes
        listeDeLignes = f.readlines()

    # Faire une liste de liste contenant les séquences de nombres (transformées de string à int)
    contenu = [[int(val) for val in lignes.split()] for lignes in listeDeLignes[0:]]

    return contenu

# TODO
def sauvegarderListesTriees(chemin, nom, listeTriees):
    # Ouvrir le fichier en mode écriture à l'aide d'un context manager
    with open(chemin + nom, "w") as f:

        # Pour tous les sequences de nombres
        for sequence in listeTriees:
            
            # Pour tous les nombres dans la séquence
            for nombre in sequence:
                # Écrire le nombre séparé d'un espace 
                f.write(str(nombre) + " ")

            # Changer de ligne
            f.write("\n")

# TODO
def fusionner(gauche, droite):
    # Si le premier tableau (gauche) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le deuxième tableau (droite) comme étant le résultat
    if len(gauche) == 0:
        return droite

    # Si le deuxième tableau (droite) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le premier tableau (gauche) comme étant le résultat
    if len(droite) == 0:
        return gauche

    resultat = []
    indexGauche = indexDroite = 0

    # Parcourir les deux tableaux jusqu'à ce que tous les éléments (droite et gauche)
    # soient ajoutés au tableau resultat
    while len(resultat) < len(gauche) + len(droite):
        # Les éléments doivent être triés pour être ajouté au tableau résultat.
        # Il faut donc décider de soit prendre le prochain élément du tableau
        # droite ou du tableau gauche
        if gauche[indexGauche] <= droite[indexDroite]:
            resultat.append(gauche[indexGauche])
            indexGauche += 1
        else:
            resultat.append(droite[indexDroite])
            indexDroite += 1

        # Si la fin de n'importe lequel des deux tableau est atteinte,
        # ajouter directement tous les éléments restants de l'autre tableau
        # au tableau résultat, et terminer la boucle.
        if indexDroite == len(droite):
            resultat += gauche[indexGauche:]
            break

        if indexGauche == len(gauche):
            resultat += droite[indexDroite:]
            break

    return resultat

# TODO
def triFusion(tableau):
    # Si le tableau contient moins de 2 elements, retouner comme étant le résultat de la fonction
    if len(tableau) < 2:
        return tableau

    # Trouver l'indice de l'élément milieu du tableau
    milieuTableau = len(tableau) // 2

    # Trier le tableau en séparant récursivement le tableau en 2 parties égales
    # qui seront triées et finalement fusionnées ensemble dans le résultat final
    # Indice: Passer à chaque paramètres de la fonction fusionner la fonction triFusion
    return fusionner(
        gauche=triFusion(tableau[:milieuTableau]),
        droite=triFusion(tableau[milieuTableau:]))

if __name__ == '__main__':
    listesATrier = lireFichier()

    print("Les listes à trier sont: ")
    print(listesATrier)

    listesTriees = []

    for sequence in listesATrier:
        listesTriees.append(triFusion(sequence))

    print("Les listes triées sont: ")
    print(listesTriees)

    sauvegarderListesTriees("./", "resultats.txt", listesTriees)
