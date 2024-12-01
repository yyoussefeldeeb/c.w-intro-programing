import unittest
import sys
sys.path.append(r"d:/codes")
from steganography import binary_to_str
class Test(unittest.TestCase):
    def test_single_char(self):
        self.assertEqual(binary_to_str([0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),"a")

    def test_empty(self):
        self.assertEqual(binary_to_str([0, 0, 0, 0, 0, 0, 0, 0]), "")

    def test_multiple_characters(self):
        self.assertEqual(binary_to_str(
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 
             0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), "abe")

if __name__ == "__main__":
    unittest.main()