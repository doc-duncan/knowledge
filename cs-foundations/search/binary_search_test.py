import unittest
import binary_search


class BinarySearchTest(unittest.TestCase):
    def test_binary_search_even_true(self):
        arr = [5,9,10,73]
        val = 73
        min_pos = 0
        max_pos = len(arr) - 1
        answer = binary_search.binary_search(arr, val, min_pos, max_pos)
        self.assertEqual(True, answer)
    
    def test_binary_search_even_false(self):
        arr = [5,9,10,73]
        val = 6
        min_pos = 0
        max_pos = len(arr) - 1
        answer = binary_search.binary_search(arr, val, min_pos, max_pos)
        self.assertEqual(False, answer)
    
    def test_binary_search_odd_true(self):
        arr = [5,9,10,55,73]
        val = 5
        min_pos = 0
        max_pos = len(arr) - 1
        answer = binary_search.binary_search(arr, val, min_pos, max_pos)
        self.assertEqual(True, answer)
    
    def test_binary_search_odd_false(self):
        arr = [5,9,10,55,73]
        val = 89
        min_pos = 0
        max_pos = len(arr) - 1
        answer = binary_search.binary_search(arr, val, min_pos, max_pos)
        self.assertEqual(False, answer)

if __name__ == '__main__':
    unittest.main()
