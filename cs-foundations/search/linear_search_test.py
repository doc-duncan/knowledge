import unittest
import linear_search

class LinearSearchTest(unittest.TestCase):
    def test_linear_search_present_odd(self):
        arr = [9,54,23,10,17]
        val = 10
        answer = linear_search.linear_search(arr,val)
        self.assertEqual(3,answer)
    
    def test_linear_search_present_even(self):
        arr = [9,54,23,10]
        val = 23
        answer = linear_search.linear_search(arr,val)
        self.assertEqual(2,answer)
    
    def test_linear_search_not_present_odd(self):
        arr = [9,54,23,10,17]
        val = 99
        answer = linear_search.linear_search(arr,val)
        self.assertEqual(-1,answer)

    def test_linear_search_not_present_even(self):
        arr = [9,54,23,10]
        val = 7
        answer = linear_search.linear_search(arr,val)
        self.assertEqual(-1,answer)
    
    def test_linear_search_not_present_empty(self):
        arr = []
        val = 0
        answer = linear_search.linear_search(arr,val)
        self.assertEqual(-1,answer)

if __name__ == '__main__':
    unittest.main()
