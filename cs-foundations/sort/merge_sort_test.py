import unittest
import merge_sort


class BubbleSortTest(unittest.TestCase):
    def test_sorted_even(self):
        arr = [9,54,3,35,20,7]
        answer = merge_sort.merge_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([3,7,9,20,35,54],answer)
    
    def test_sorted_odd(self):
        arr = [9,60,54,3,35,20,7]
        answer = merge_sort.merge_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([3,7,9,20,35,54,60],answer)

    def test_sorted_one(self):
        arr = [3]
        answer = merge_sort.merge_sort_recursive(arr,0, len(arr)-1)
        self.assertEqual([3],answer)


if __name__ == '__main__':
    unittest.main()
