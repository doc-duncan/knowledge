import unittest
import bubble_sort


class BubbleSortTest(unittest.TestCase):
    def test_sorted_even(self):
        arr = [9,54,3,35,20,7]
        answer = bubble_sort.bubble_sort_iterative(arr,len(arr))
        self.assertEqual([3,7,9,20,35,54],answer)
    
    def test_sorted_odd(self):
        arr = [9,60,54,3,35,20,7]
        answer = bubble_sort.bubble_sort_iterative(arr,len(arr))
        self.assertEqual([3,7,9,20,35,54,60],answer)

    def test_sorted_one(self):
        arr = [3]
        answer = bubble_sort.bubble_sort_iterative(arr,len(arr))
        self.assertEqual([3],answer)

    def test_sorted_empty(self):
        arr = []
        answer = bubble_sort.bubble_sort_iterative(arr,len(arr))
        self.assertEqual([],answer)

if __name__ == '__main__':
    unittest.main()
