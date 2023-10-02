import unittest
from Cryptage import crypt

class TestCryptage(unittest.TestCase):
    def test_crypt(self):
        self.assertEqual(crypt("Hello"), "Ifmmp")

if __name__ == '__main__':
    unittest.main()
