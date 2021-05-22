"""
Bubble Sort

Algorithm:
1. For each index (idx_a) in a given list
    a. Compare the values in list at idx_a and (idx_a + 1)
    b. If value value at idx_a > value at (idx_a + 1) then swap
"""

def bubble_sort_iterative(arr, arr_len):
    for track in range(arr_len):
        for idx in range(arr_len - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr
        
