def binary_search(arr, val, min_pos, max_pos):
    """Returns boolean representing if val is in arr."""
    if max_pos >= min_pos:
        mid_pos = ((max_pos - min_pos) // 2) + min_pos
        mid_val = arr[mid_pos]
        if val == mid_val:
            return True
        elif val > mid_val:
            return binary_search(arr, val, mid_pos + 1, max_pos)
        elif val < mid_val:
            return binary_search(arr, val, 0, mid_pos - 1)
    else:
        return False
