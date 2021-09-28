import unittest
import picnic.math.func as func

class FuncTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(func.add(5,3), 8, 
                      "Does not add properly")

    def test_sub(self):
        self.assertEqual(func.sub(5, 3), 2, 
                      "Does not subtract properly")

if __name__ == '__main__':
    unittest.main()
