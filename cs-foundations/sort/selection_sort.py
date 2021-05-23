"""
Selection Sort

Algorithm:
1. For each index (index_a) in the given list
    a. Get the value at index_a
    b. For each index (index_b) in the range (index_a + 1, len(list))
        1. Initialize the lowest value to the value at index_a
        2. If the value at index_b is greater than the lowest value then set lowest to value at index_b
    c. Put lowest value at index_a and swap if necessary
"""
def selection_sort(arr,length):
    """Returns a sorted version of the given arr."""
    for min_pos in range(length):
        min_index = min_pos
        for tracker in range(min_pos+1,length):
            if arr[tracker] < arr[min_index]:
                min_index = tracker
        if min_index != min_pos:
            arr[min_pos], arr[min_index] = arr[min_index], arr[min_pos]
    return arr

def selection_sort_recursive(arr,min_pos,length):
    """Returns a sorted version of the given arr."""
    if length == 0:
        return []
    if min_pos == (length-1):
        return arr
    else:
        min_index = get_min_index_recursive(arr,min_pos,length)
        if min_index != min_pos:
            arr[min_pos], arr[min_index] = arr[min_index], arr[min_pos]
        return selection_sort_recursive(arr,min_pos+1,length)

def get_min_index_recursive(arr,min_pos,length):
    """Returns the minimum index in the arr."""
    if min_pos == (length-1):
        return min_pos
    else:
        subset_min_pos = get_min_index_recursive(arr,min_pos+1,length)
        return min_pos if arr[min_pos] < arr[subset_min_pos] else subset_min_pos
