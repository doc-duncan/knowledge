import unittest
import quick_sort


class QuickSortTest(unittest.TestCase):
    def test_sorted_even(self):
        arr = [9,54,3,35,20,7]
        quick_sort.quick_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([3,7,9,20,35,54],arr)
    
    def test_sorted_odd(self):
        arr = [9,60,54,3,35,20,7]
        quick_sort.quick_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([3,7,9,20,35,54,60],arr)

    def test_sorted_one(self):
        arr = [3]
        quick_sort.quick_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([3],arr)

    def test_sorted_empty(self):
        arr = []
        quick_sort.quick_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([],arr)

if __name__ == '__main__':
    unittest.main()