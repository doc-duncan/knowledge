import unittest
import selection_sort


class SelectionSortTest(unittest.TestCase):
    def test_sorted_even(self):
        arr = [9,54,3,35,20,7]
        answer = selection_sort.selection_sort(arr,len(arr))
        self.assertEqual([3,7,9,20,35,54],answer)
    
    def test_sorted_odd(self):
        arr = [9,60,54,3,35,20,7]
        answer = selection_sort.selection_sort(arr,len(arr))
        self.assertEqual([3,7,9,20,35,54,60],answer)

    def test_sorted_one(self):
        arr = [3]
        answer = selection_sort.selection_sort(arr,len(arr))
        self.assertEqual([3],answer)

    def test_sorted_empty(self):
        arr = []
        answer = selection_sort.selection_sort(arr,len(arr))
        self.assertEqual([],answer)

    def test_sorted_recursive_even(self):
        arr = [9,54,3,35,20,7]
        answer = selection_sort.selection_sort_recursive(arr,0,len(arr))
        self.assertEqual([3,7,9,20,35,54],answer)
    
    def test_sorted_recursive_odd(self):
        arr = [9,60,54,3,35,20,7]
        answer = selection_sort.selection_sort_recursive(arr,0,len(arr))
        self.assertEqual([3,7,9,20,35,54,60],answer)

    def test_sorted_recursive_one(self):
        arr = [3]
        answer = selection_sort.selection_sort_recursive(arr,0,len(arr))
        self.assertEqual([3],answer)

    def test_sorted_recursive_empty(self):
        arr = []
        answer = selection_sort.selection_sort_recursive(arr,0,len(arr))
        self.assertEqual([],answer)

    def test_min_index_even(self):
        arr = [9,54,3,35,2,7]
        answer = selection_sort.get_min_index_recursive(arr,0,len(arr))
        self.assertEqual(4,answer)
    
    def test_min_index_odd(self):
        arr = [9,60,54,3,35,2,7]
        answer = selection_sort.get_min_index_recursive(arr,0,len(arr))
        self.assertEqual(5,answer)

    def test_min_index_one(self):
        arr = [3]
        answer = selection_sort.get_min_index_recursive(arr,0,len(arr))
        self.assertEqual(0,answer)

if __name__ == '__main__':
    unittest.main()
