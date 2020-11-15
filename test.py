import exo1 as tri
import exo2 as dijkstra
import numpy as np
from random import randint
import unittest
import os
import sys

class TestTriFusion(unittest.TestCase):
    
    def test_deja_trie(self):
        a_trier = [0,1,2,3,4,5,6,7,8,9]

        tri_etudiant = tri.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_repetition(self):
        a_trier = [1,1,1,1,1,1]

        tri_etudiant = tri.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_repetition2(self):
        a_trier = [1,1,1,0,1,1]

        tri_etudiant = tri.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_negatif(self):
        a_trier = [-5, -2, 1, 456, -34, 0]

        tri_etudiant = tri.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_gros(self):
        a_trier = np.random.rand(500).tolist()

        tri_etudiant = tri.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier) 

class TestDijkstra(unittest.TestCase):
    def test_lire_poids(self):

        poids_attendus = [[0, -1, -1, 2, -1, -1, 8, -1], [1, 0, -1, -1, -1, -1, -1, 3], [-1, 1, 0, -1, -1, 2, 3, -1], [2, -1, -1, 0, -1, -1, 4, -1], [5, 3, 2, -1, 0, -1, -1, -1], [-1, -1, 1, 3, 5, 0, -1, 4], [-1, 2, 1, -1, -1, 4, 0, -1], [-1, -1, 2, -1, 2, -1, -1, 0]]       
        
        self.assertEqual(dijkstra.lire_poids("poids.txt"), poids_attendus)

    def test_initialiser(self):
        nNoeuds = 10
        noeud_initial = 2
        AUCUN = -1

        distances_attendues = [AUCUN] * nNoeuds
        distances_attendues[noeud_initial] = 0

        # TODO: - Les predecesseurs sont initialisés a -1.
        predecesseurs_attendus = [AUCUN] * nNoeuds
        predecesseurs_attendus[noeud_initial] = 0

        # TODO: - Noeuds doit etre initialise pour contenir toutes les valeurs de 0 a nNoeuds-1.
        noeuds_attendus = []
        for i in range(nNoeuds):
            noeuds_attendus.append(i)
        
        resultat_etudiant = dijkstra.initialiser(noeud_initial, nNoeuds)

        self.assertEqual((distances_attendues, predecesseurs_attendus, noeuds_attendus),(resultat_etudiant[0], resultat_etudiant[1], resultat_etudiant[2]))

    def trouver_element_plus_proche():
        poids = [[0, -1, -1, 2, -1, -1, 8, -1], [4, 0, -1, 5, -1, -1, -1, 3], [-1, 1, 0, -1, -1, 2, 3, -1], [2, -1, -1, 0, -1, -1, 4, -1], [5, 3, 2, -1, 0, -1, -1, 
                -1], [-1, -1, 1, 3, 5, 0, -1, 4], [-1, 2, 3, -1, -1, 4, 0, -1], [-1, -1, 2, -1, 2, -1, -1, 0]]

        

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)