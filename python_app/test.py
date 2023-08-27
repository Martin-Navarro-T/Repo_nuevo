import unittest
from hello import suma
class TestSuma(unittest.TestCase):
    def test_init(self):
        self.assertEqual(sum(2,2),4)
        
if __name__=="__main__":
    unittest.main()