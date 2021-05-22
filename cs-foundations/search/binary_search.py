"""
Binary Search

This searching algorithm requires a sorted list.

Algorithm:
1. Is your list empty?
    Yes: return False
    No: proceed to step 2
2. Find the middle element of the list
3. Is this middle element equal to your target element?
    Yes: return True
    No: proceed to step 4
4. Is your target element larger or smaller than this middle element?
    Larger: perform the process again with a sub-list equal to everything AFTER the middle element
    Smaller: perform the process again with a sub-list equal to everything BEFORE the middle element

Time Complexity:
O(logn)
"""

def binary_search_recursive(arr, val, min_pos, max_pos):
    """Returns boolean representing if val is in arr."""
    if max_pos >= min_pos:
        mid_idx = (max_pos + min_pos) / 2
        mid_ele = arr[mid_idx]
        if mid_ele == val:
            return True
        elif mid_ele > val:
            return binary_search_recursive(arr, val, min_pos, mid_idx - 1)
        else:
            return binary_search_recursive(arr, val, mid_idx + 1, max_pos)
    else:
        return False

def binary_search_iterative(arr, val):
    """Returns boolean representing if val is in arr."""
    min_pos = 0
    max_pos = len(arr) - 1

    while max_pos >= min_pos: 
        mid_idx = (max_pos + min_pos) / 2
        mid_ele = arr[mid_idx]
        if mid_ele == val:
            return True
        if mid_ele > val:
            max_pos = mid_idx - 1
        else:
            min_pos = mid_idx + 1

    return False
