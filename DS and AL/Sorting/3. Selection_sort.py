def find_min(arr):

    # O(n)
    min_ = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_: min_ = arr[i]
    return min_

def selection_sort(arr):

    ret_list = []
    while len(arr)!=0:
        min_ = find_min(arr)
        arr.remove(min_)
        ret_list.append(min_)
    return ret_list

selection_sort(arr=[5, 0, 6, 10, 2, -1])