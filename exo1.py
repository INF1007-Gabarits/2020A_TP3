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
def trierListe(listeATrier):
    # Tant que sommet < taille - 1
    for sommet in range(len(listeATrier) - 1):
        # Initialiser la position du plus petit
        indicePlusPetit = sommet

        # Trouver le plus petit élément de la zone de tri effective
        for indice in range(sommet + 1, len(listeATrier), 1):
            if listeATrier[indice] < listeATrier[indicePlusPetit]:
                indicePlusPetit = indice
        
        # Si nécessaire, déplacer le plus petit élément au sommet
        if indicePlusPetit != sommet:
            listeATrier[indicePlusPetit], listeATrier[sommet] = listeATrier[sommet], listeATrier[indicePlusPetit] 

    return listeATrier

if __name__ == '__main__':
    listesATrier = lireFichier()

    print(listesATrier)

    listesTriees = []

    for sequence in listesATrier:
        listesTriees.append(trierListe(sequence))

    print(listesTriees)

    sauvegarderListesTriees("./", "resultats.txt", listesTriees)
