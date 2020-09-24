import inspect

#region constantes

TAILLE_MAX = 32
AUCUN = -1; # Valeur utilisee lorsqu'il n'y a aucun chemin, aucun predecesseur, etc.  Pour utiliser une constante unique, il faut qu'elle ait une valeur invalide a la fois comme distance et comme numero de noeud.

#endregion

#region fonctions d'aide

# Indique si un element est dans l'ensemble.
def estDans(ensemble, element):
    for elem in ensemble:
        if elem == element:
            return True

    return False

def comparerTableaux(tableauA, tableauB):
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[len(tableauA) == len(tableauB)])

    estPareil = True
    for i in range(len(tableauA)):
        if tableauA[i] != tableauB[i]:
            estPareil = False

    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[estPareil])

def afficherTableau(nomTableau, tableau):
    print("Affichage tableau: " + nomTableau)

    for elem in tableau:
        print("{0:4}".format(elem), end=" ")
    print()

def afficherMatrice(nomMatrice, matrice):
    print("Affichage du contenu de la matrice: " + nomMatrice)
    for line in matrice:
        for elem in line:
            print("{0:4}".format(elem), end=" ")
        print()

#endregion

#region fonctions a completer

def trouveElementPlusProche(distances, noeuds):
    return 1

def mettreAJourDistances(poids, distances, predecesseurs, noeuds, parNoeud):
    return

def retirerUnElementDuTableau(ensemble, element):
    return

#endregion

#region "Fonctions de test"

BON_SI_VRAI = ["ERREUR", "BON"]

def tester_trouveElementPlusProche():
    print("Test de trouveElementPlusProche:")
    
    distances = [7, 2, -1 , 5, 6]
    noeuds = [0, 1 , 2, 3, 4]
    
    plusProche = trouveElementPlusProche(distances, noeuds)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plusProche == 1])

    noeuds = [0, 2, 3, 4]
    plusProche = trouveElementPlusProche(distances, noeuds)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plusProche == 3])

def tester_mettreAJourDistances():
    print("Test de mettreAJourDistances")
    poids = [[0,  4,  2, -1], [-1,  0, -1,  2], [1,  1,  0,  6], [-1, -1, -1,  0]]
    distances = [0, -1, -1, -1]
    predecesseurs = [-1, -1, -1, -1]

    noeuds = [0, 1, 2, 3 ]
    distancesAttendues = [0, 4, 2, -1 ]
    predecesseursAttendus = [-1, 0, 0, -1 ]
    mettreAJourDistances(poids, distances, predecesseurs, noeuds, 0)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(distances, distancesAttendues)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(predecesseurs, predecesseursAttendus)
    distances = distancesAttendues
    predecesseurs = predecesseursAttendus

    noeuds = [1, 2, 3 ]
    distancesAttendues = [0, 3, 2, 8 ]
    predecesseursAttendus = [-1, 2, 0, 2 ]


    mettreAJourDistances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(distances, distancesAttendues)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(predecesseurs, predecesseursAttendus)
    distances = distancesAttendues
    predecesseurs = predecesseursAttendus

    # Un etat impossible dans l'algorithme, mais ceci permet de verifier si mettreAJourDistances verifie seulement les elements de l'ensemble noeuds.
    distances[0] = 10
    noeuds = [1, 2, 3 ]
    mettreAJourDistances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[distances[0] == 10])

def tester_retirerUnElementDuTableau():
    print("Test de retirerUnElementDuTableau: ")
    ensemble = [5, 2, 3, 4, 1]
    ensembleSans2 = [1, 4, 3, 5] #C'est un ensemble, l'ordre n'est pas important
    retirerUnElementDuTableau(ensemble, 2)
    print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[len(ensemble) == len(ensembleSans2)])
    for elem in ensembleSans2:
        print("Test a la ligne "+ str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[estDans(ensemble, elem)])

#endregion

if __name__ == '__main__':
    tester_trouveElementPlusProche()
    tester_mettreAJourDistances()
    tester_retirerUnElementDuTableau()
    print("Fin des tests")

	# //TODO: Lire la matrice des poids � partir du fichier poids.txt.
	# bool ok = true;
	# Matrice matriceLue = lirePoids("poids.txt", ok); //Devrait mettre une constante pour poids.txt

	#  //TODO: Afficher un message d'erreur si la lecture �choue, et ne pas continuer l'ex�cution.
	# if (!ok)
	# {
	# 	cout << "La lecture a echoue";
	# 	return 0;
	# }

	# //TODO: Demander � l'utilsateur l'indice du noeud source, avec validation de l'entr�e.
	# unsigned indiceNoeudSource;
	# do {
	# 	cout << "Quel est l'indice du noeud source? ";
	# 	cin >> indiceNoeudSource;
	# } while (indiceNoeudSource < 0 || indiceNoeudSource > matriceLue.taille - 1); // pas sur de cette condition

	# //TODO: Intialiser les tableaux de distances, predecesseurs et noeuds.
	# Tableau tableauDistances,
	# 	tableauPredecesseurs,
	# 	tableauNoeuds;
	# initialiser(tableauDistances, tableauPredecesseurs, tableauNoeuds, indiceNoeudSource, matriceLue.taille);

	# //TODO: Tant qu'il reste des �l�ments dans l'ensemble noeuds:
	# while (tableauNoeuds.taille != 0)
	# {
	# 	//TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.
	# 	int elementPlusProche = trouveElementPlusProche(tableauDistances, tableauNoeuds);
	# 	//TODO: Mettre � jour les distances en v�rifiant si c'est plus court de passer par le noeud le plus proche.
	# 	mettreAJourDistances(matriceLue, tableauDistances, tableauPredecesseurs, tableauNoeuds, elementPlusProche);
	# 	//TODO: Retirer cet element le plus proche de l'ensemble noeuds.
	# 	retirerUnElementDuTableau(tableauNoeuds, elementPlusProche);
	# }



	# //TODO: Afficher le contenu de distances.
	# afficherTableau("Contenu de distances", tableauDistances);
	# //TODO: Afficher le contenu de predecesseurs.
	# afficherTableau("Contenu de predecesseurs", tableauPredecesseurs);
	# //TODO: Demander � l'utilisateur un noeud destination diff�rent la source, avec validation de l'entr�e.
	# unsigned indiceNoeudDestination;
	# do {
	# 	cout << "Quel est l'indice du noeud destination? ";
	# 	cin >> indiceNoeudDestination;
	# } while (indiceNoeudDestination < 0 || indiceNoeudDestination > matriceLue.taille - 1); // pas sur de cette condition
	# 																						//TODO: Afficher la solution, soit le plus court chemin allant de la source vers la destination.
	# afficherCheminPlusProche(tableauDistances, tableauPredecesseurs, indiceNoeudSource, indiceNoeudDestination);
