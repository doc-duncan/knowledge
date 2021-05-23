"""
Merge Sort

Algorithm
1. If the given list is of length 1 then return that list
2. Split the list into two halvs
3. Call the sort function on the two halves and merge them together (merging two sorted lists is linear time)
"""

def merge_sort_recursive(arr, min_pos, max_pos):
    if min_pos >= max_pos:
        return [arr[max_pos]]
    mid_idx = (min_pos + max_pos) / 2
    return merge(merge_sort_recursive(arr, min_pos, mid_idx), merge_sort_recursive(arr, mid_idx + 1, max_pos))

def merge(arr_one, arr_two):
    new_arr = []
    i, j = 0, 0
    while len(new_arr) < (len(arr_one) + len(arr_two)):
        if i == len(arr_one):
            new_arr += arr_two[j:]
        elif j == len(arr_two):
            new_arr += arr_one[i:]
        else:   
            one_val = arr_one[i]
            two_val = arr_two[j]
            if one_val < two_val:
                new_arr.append(one_val)
                i += 1
            else:
                new_arr.append(two_val)
                j += 1
    return new_arr
