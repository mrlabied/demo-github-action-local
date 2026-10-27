
import unittest
from calcul import addition

class TestCalcul(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
