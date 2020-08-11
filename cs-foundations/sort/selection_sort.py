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
