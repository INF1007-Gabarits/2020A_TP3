import inspect

# region constantes
#        Si nécessaire ajoutez vos constantes ici afin de ne pas utiliser de chiffres magiques dans le code

TAILLE_MAX = 32
AUCUN = -1  # Valeur utilisee lorsqu'il n'y a aucun chemin, aucun predecesseur, etc.  Pour utiliser une constante unique,
# il faut qu'elle ait une valeur invalide a la fois comme distance et comme numero de noeud.

# endregion

# region "Fonctions d'aide, Rien à modifier ici!"

# Indique si un element est dans l'ensemble.
def est_dans(ensemble, element):
    for elem in ensemble:
        if elem == element:
            return True

    return False


def comparer_listes(tableauA, tableauB):
    print(
        "Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[len(tableauA) == len(tableauB)])

    estPareil = True
    for i in range(len(tableauA)):
        if tableauA[i] != tableauB[i]:
            estPareil = False

    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[estPareil])


def afficher_liste(nomTableau, tableau):
    print("Affichage tableau: " + nomTableau)

    for elem in tableau:
        print("{0:4}".format(elem), end=" ")
    print()


def afficher_matrice(nomMatrice, matrice):
    print("Affichage du contenu de la matrice: " + nomMatrice)
    for line in matrice:
        for elem in line:
            print("{0:4}".format(elem), end=" ")
        print()


# endregion

# region "Fonction à compléter"

# 1- Lit la matrice poids (distances entre les villes) a partir d'un fichier. Retourne le contenu de la matrice lue
def lire_poids(nomFichier):
    # TODO: Lire le fichier et verifier que la lecture n'a pas fait d'erreur; affecter la valeur a ok selon s'il y a eu
    #      une erreur ou non et retourner la matrice lue.  La matrice retournée n'a pas d'importance s'il y a eu une erreur.
    #      Format du fichier: dimension sur une ligne puis les differents elements séparés par des "whitespaces".
    #
    # TODO : Ajouter une couche de vérification des données en entrée. Vérifier que toutes les lignes de la matrice
    #                ont la même longeur et qu'il n'y a pas de valeurs incohérentes (autres que des entier positifs ou -1). Si la matrice est
    #                non conforme, utilisez la fonction exit() pour terminer le programme après avoir notifié l'utilisateur. 

    return matrice_lue


# 2- Initialise les structures pour appliquer l'algorithme de Dijkstra.
def initialiser(noeudInitial, nNoeuds):
    # TODO: Initialiser et retourne les tableaux distances, predecesseurs et noeuds, incluant leurs tailles.
    #       Tel qu'indique dans l'enonce:
    #       Les distances sont initialisees a -1 sauf pour le noeud initial qui est a 0.

    # TODO: - Les predecesseurs sont initialisés a -1.
    # TODO: - Noeuds doit etre initialise pour contenir toutes les valeurs de 0 a nNoeuds-1.

    return distances, predecesseurs, noeuds


# 3 - Trouve et retourne l'élément le plus proche de l'élément initial, selon le tableau actuel des distances.
def trouver_element_plus_proche(distances, noeuds):
    # TODO: Pour chaque element de la liste de noeuds, vérifier lequel a la plus petite valeur dans les distances et
    #  retourner l 'indice de cet élément. distance_min = AUCUN

    return ...


# 4 - Fait la mise à jour des distances et des predecesseurs si on permet de passer par parNoeud. Cette fonction ne
#     retourne rien elle modifie les paramètres référencés directement.
def mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, parNoeud):
    # TODO: Pour chaque element de l'ensemble noeuds, vérifier si passer parNoeud pour y aller réduit la distance
    #       par rapport à celle actuellement dans le tableau distances; si c'est le cas, modifie la distance pour
    #       cette nouvelle valeur et change le prédécesseur de cet élément comme étant parNoeud.  Attention aux valeurs -1
    #       dans les poids et les distances.  Voir la description dans l'énoncé pour plus de détails.
    ...


# 5- Affiche le plus court chemin, soit la liste des noeuds par lesquels il faut passer pour se rendre de la source
#    a la destination. Suppose que l'algorithme a deja ete applique pour calculer les tableaux de distances et predecesseurs.
#    Cette fonction ne retourne rien.
def afficher_chemin_plus_proche(distances, predecesseurs, noeudSource, noeudDestination):
    # TODO: Afficher le chemin similairement à l'exemple de sortie suivant:
    #       Le chemin le plus court de 4 vers 7 est:
    #       4 -> 2 -> 5 -> 7
    #       de distance 10
    ...


# endregion

# region "Fonctions de test - Rien à modifier pour vous ici!"

BON_SI_VRAI = ["ERREUR", "BON"]


def tester_trouver_element_plus_proche():
    print("Test de trouveElementPlusProche:")

    distances = [7, 2, -1, 5, 6]
    noeuds = [0, 1, 2, 3, 4]

    plus_proche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plus_proche == 1])

    noeuds = [0, 2, 3, 4]
    plus_proche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plus_proche == 3])


def tester_mettre_a_jour_distances():
    print("Test de mettre_a_jour_distances")
    poids = [[0, 4, 2, -1], [-1, 0, -1, 2], [1, 1, 0, 6], [-1, -1, -1, 0]]
    distances = [0, -1, -1, -1]
    predecesseurs = [-1, -1, -1, -1]

    noeuds = [0, 1, 2, 3]
    distances_attendues = [0, 4, 2, -1]
    predecesseurs_attendus = [-1, 0, 0, -1]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 0)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : Deux sous tests")
    comparer_listes(distances, distances_attendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : Deux sous tests")
    comparer_listes(predecesseurs, predecesseurs_attendus)
    distances = distances_attendues
    predecesseurs = predecesseurs_attendus

    noeuds = [1, 2, 3]
    distances_attendues = [0, 3, 2, 8]
    predecesseurs_attendus = [-1, 2, 0, 2]

    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparer_listes(distances, distances_attendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparer_listes(predecesseurs, predecesseurs_attendus)
    distances = distances_attendues
    predecesseurs = predecesseurs_attendus

    # Un etat impossible dans l'algorithme, mais ceci permet de verifier si mettreAJourDistances verifie seulement les elements de l'ensemble noeuds.
    distances[0] = 10
    noeuds = [1, 2, 3]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[distances[0] == 10])



# endregion

if __name__ == '__main__':
    tester_trouver_element_plus_proche()
    tester_mettre_a_jour_distances()
    print("Fin des tests")

    # TODO: Lire la matrice des poids à partir du fichier poids.txt et l'afficher dans le terminal.

    # TODO: Demander a l'utilsateur l'indice du noeud source, avec validation de l'entree.

    # TODO: Intialiser les tableaux de distances, predecesseurs et noeuds.

    # TODO: Tant qu'il reste des éléments dans l'ensemble noeuds:
        # 	TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.

        #   TODO: Si tous les chemins possibles ont été évalués (aucun prochain element a visiter), sortir de la boucle

        # 	TODO: Mettre à jour les distances en vérifiant si c'est plus court de passer par le noeud le plus proche.

        # 	TODO: Retirer cet element le plus proche de l'ensemble noeuds.

    # TODO: Afficher le contenu de distances.

    # TODO: Afficher le contenu de predecesseurs.

    # TODO: Demander a l'utilisateur un noeud destination different de la source, avec validation de l'entree (indiquer
    #       l'intervalle de sommet possible et si la valeur entrée est hors de celui-ci).

    # TODO: Valider si un chemin entre les deux sommet existe
    # TODO: Afficher la solution, soit le plus court chemin allant de la source vers la destination.


    
