import unittest

def trouver_deux_valeurs(s, t):
    vv = {}
    for i, v in enumerate(s):
        c = t - v
        if c in vv:
            return (vv[c], i)
        vv[v] = i
    return None


class TestTrouverDeuxValeurs(unittest.TestCase):

    def test_paire_existe(self):
        s = [10, 22, 5, 75, 65, 80]
        t = 70
        r = trouver_deux_valeurs(s, t)
        self.assertIsNotNone(r)
        i, j = r
        self.assertEqual(s[i] + s[j], t)

    def test_aucune_paire(self):
        s = [1, 2, 3, 4]
        t = 100
        r = trouver_deux_valeurs(s, t)
        self.assertIsNone(r)

    def test_valeurs_negatives(self):
        s = [-5, 10, 15, -10, 20]
        t = 5
        r = trouver_deux_valeurs(s, t)
        self.assertIsNotNone(r)
        i, j = r
        self.assertEqual(s[i] + s[j], t)

    def test_zero_target(self):
        s = [-1, 0, 1]
        t = 0
        r = trouver_deux_valeurs(s, t)
        self.assertIsNotNone(r)
        i, j = r
        self.assertEqual(s[i] + s[j], t)

    def test_duplicats(self):
        s = [5, 5, 10]
        t = 10
        r = trouver_deux_valeurs(s, t)
        self.assertIsNotNone(r)
        i, j = r
        self.assertNotEqual(i, j)
        self.assertEqual(s[i] + s[j], t)

if __name__ == "__main__":
    unittest.main()
