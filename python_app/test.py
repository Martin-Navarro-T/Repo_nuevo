import unittest
from hello import suma
class TestSuma(unittest.TestCase):
    def test_init(self):
        self.assertEqual(suma(2,2),4)
        
