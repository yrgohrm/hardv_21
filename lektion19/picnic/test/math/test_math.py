import unittest
import picnic.math.func as func


class FuncTests(unittest.TestCase):
    def setUp(self):
        print("Innan metod")

    def tearDown(self):
        print("Efter metod")

    @classmethod
    def setUpClass(cls):
        print("Innan klass")

    @classmethod
    def tearDownClass(cls):
        print("Efter klass")

    def test_add(self):
        self.assertEqual(func.add(5, 3), 8,
                         "Does not add properly")

    def test_add_negative(self):
        self.assertEqual(func.add(-5, -3), -8,
                         "Does not add properly")

    def test_sub(self):
        self.assertEqual(func.sub(5, 3), 2,
                         "Does not subtract properly")

    def test_sub_zero(self):
        for i in [1, 2, -334, 9999999]:
            self.assertEqual(func.sub(i, 0), i,
                             "Does not subtract properly")


if __name__ == '__main__':
    unittest.main()
