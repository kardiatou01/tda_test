import unittest
from Cryptage import crypt

class TestCryptage(unittest.TestCase):
    def test_crypt(self):
        self.assertEqual(crypt("Hello", 1), "Ifmmp1")

    def test_crypt_avec_pas(self):
        self.assertEqual(crypt("Hello", 3), "Khoor3")

if __name__ == '__main__':
    unittest.main()

