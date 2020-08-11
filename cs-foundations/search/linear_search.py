def linear_search(arr, val):
    """Returns index of val in arr if present, if not returns -1."""
    for index, key in enumerate(arr):
        if key == val:
            return index
    return -1
