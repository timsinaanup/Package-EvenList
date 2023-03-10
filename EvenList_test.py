import unittest
import EvenList

class TestEvenList(unittest.TestCase):
    def test_even(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even_lst = EvenList.EvenList(lst)
        self.assertEqual(even_lst.even(), [2, 4, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()
