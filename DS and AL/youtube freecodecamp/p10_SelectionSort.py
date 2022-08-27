def find_min(arr):
    min_ = arr[0]
    for i in arr:
        if i < min_:
            min_ = i
    return min_

def selection_sort(main_arr):
    arr_ = main_arr.copy()
    sorted_l = []

    while arr_:
        min_ = min(arr_)
        arr_.remove(min_)
        sorted_l.append(min_)

    return sorted_l

main_arr = [5, 1, 6, 0, 1]
selection_sort(main_arr)