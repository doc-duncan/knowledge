"""
Quick Sort

The goal is to get everything on the left of the pivot less than it and everything on the right of it greater.
Then just call recursively on the two smaller lists.

helper video: https://www.youtube.com/watch?v=ZHVk2blR45Q

Algorithm:
1. Given a list, select the last value in the list as your "pivot" point
2. Create two counters and initialize them both to the beginning of the list
    a. "i" will represent your current location in the list
    b. "j" will represent the index of the "first" value that is greater than the pivot value
3. While "i" is less than the last index of the list
    a. If the value at index "i" is less than the pivot value then swap the values of list[i] and list[j] and then increment "j"
4. Swap the values at index of "j" and pivot
"""

def quick_sort_recursive(arr, min_pos, max_pos):
    if min_pos >= max_pos:
        return
    pivot_idx = max_pos
    pivot_val = arr[pivot_idx]
    i, j = min_pos, min_pos
    while i < (max_pos):
        i_val = arr[i]
        if i_val < pivot_val:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
    arr[j], arr[pivot_idx] = arr[pivot_idx], arr[j]
    pivot_idx = j
    quick_sort_recursive(arr, min_pos, pivot_idx - 1)
    quick_sort_recursive(arr, pivot_idx + 1, max_pos)