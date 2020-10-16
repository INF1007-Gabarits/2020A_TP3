# TODO Fonction retournant les séquences à trier, lues à partir d'un fichier
def lireFichier():
    chemin = "./"
    nom = "listeDeNombres.txt"

    # Ouvrir le fichier en mode de lecture à l'aide d'un context manager

        #Lire les lignes du fichier dans un tableau de lignes


    # Faire une tableau de tableau (contenu) contenant les séquences de nombres (transformées de string à int)


    return contenu

# TODO Fonction écrivant les séquences triées dans un fichier spécifié
def sauvegarderSequencesTriees(chemin, nom, sequencesTriees):
    ...
    # Ouvrir le fichier en mode écriture à l'aide d'un context manager


        # Pour toutes les séquences triées de nombres

            
            # Pour tous les nombres dans la séquence

                # Écrire le nombre suivi d'un espace 


            # Changer de ligne


# TODO Fonction servant à joindre les deux tableaux ensemble, avec les éléments en ordre croissant
def fusionner(gauche, droite):
    # Si le premier tableau (gauche) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le deuxième tableau (droite) comme étant le résultat



    # Si le deuxième tableau (droite) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le premier tableau (gauche) comme étant le résultat



    resultat = []
    indexGauche = indexDroite = 0

    # Boucler jusqu'à ce que tous les éléments des deux tableaux (droite et gauche)
    # soient ajoutés au tableau resultat 

        # Les éléments doivent être triés pour être ajouté au tableau résultat.
        # Il faut donc décider de soit prendre le prochain élément du tableau
        # droite ou soit du tableau gauche







        # Si la fin de n'importe lequel des deux tableaux est atteinte,
        # ajouter directement tous les éléments restants de l'autre tableau
        # au tableau résultat, et terminer la boucle.








    return resultat

# TODO Fonction d'entrée du tri fusion
def triFusion(sequenceDeNombre):
    ...
    # Si le tableau (sequenceDeNombre) contient moins de 2 éléments, retourner directement le tableau
    # comme étant le résultat de la fonction



    # Trouver l'indice de l'élément milieu du tableau


    # Trier le tableau en séparant récursivement le tableau en 2 parties égales
    # qui seront triées et finalement fusionnées ensemble dans le résultat final
    # INDICE: Passer à chaque paramètres de la fonction fusionner la fonction triFusion
    # avec une partie (gauche ou droite) de la séquence de nombre




# NE PAS TOUCHER, C'EST UNE FONCTION DE TEST POUR VOUS AIDER À VALIDER VOS RÉSULTATS
def testerResultat(sequencesATrier, sequencesTriees):
    bonResultats = 0

    for indice in range(len(sequencesTriees)):
        test = sequencesATrier[indice][:] 
        test.sort() # C'est facile le Python ! 
        if (test == sequencesTriees[indice]): 
            bonResultats += 1

    return bonResultats == len(sequencesATrier)

# NE PAS TOUCHER AU MAIN
if __name__ == '__main__':
    sequencesATrier = lireFichier()

    print("Les séquences à trier sont: ")
    print(sequencesATrier)

    sequencesTriees = []

    for sequence in sequencesATrier:
        sequencesTriees.append(triFusion(sequence))

    print("Les séquences triées sont: ")
    print(sequencesTriees)

    estBon = testerResultat(sequencesATrier, sequencesTriees)

    if estBon:
        print("Bravo, le tri est bon !")  
    else:
        print("Oups, le tri ne fonctionne pas")
    
    sauvegarderSequencesTriees("./", "resultats.txt", sequencesTriees)
