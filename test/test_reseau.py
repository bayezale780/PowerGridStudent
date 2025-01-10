import unittest
from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):
    def test_definition_entree(self):
        r = Reseau()
        r.ajouter_noeud(0, (0, 0))
        r.definir_entree(0)
        self.assertEqual(r.noeud_entree, 0)

    def test_ajout_noeud(self):
        r = Reseau()
        r.ajouter_noeud(1, (1, 1))
        self.assertIn(1, r.noeuds)

    def test_validation_correcte(self):
        r = Reseau()
        r.ajouter_noeud(0, (0, 0))
        r.definir_entree(0)
        r.ajouter_noeud(1, (1, 0))
        r.ajouter_arc(0, 1)
        self.assertTrue(r.valider_reseau())

if __name__ == "__main__":
    unittest.main()
