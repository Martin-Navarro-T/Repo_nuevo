import unittest
from hello import x
class TestSuma(unittest.TestCase):
    def test(self):
        self.assertEqual(x,4)
        
if __name__=="__main__":
    unittest.main()