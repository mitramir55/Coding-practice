import random
def merge_sort(arr, start, end):
    print(f'start = {start}')
    print(f'end = {end}')

    if end - start <2: return arr[start: end]
    mid_idx = (end - start) // 2 + start

    sorted_arr_right = merge_sort(arr, start=mid_idx, end=end)
    sorted_arr_left = merge_sort(arr, start, end=mid_idx)

    return compare_and_merge(sorted_arr_left, sorted_arr_right)

def compare_and_merge(left_arr, right_arr):

    i, j = 0, 0
    ret_l = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            ret_l.append(left_arr[i])
            i += 1
        else: 
            ret_l.append(right_arr[j])
            j += 1

    # is there anything remaining?
    while i < len(left_arr): 
        ret_l.append(left_arr[i])
        i += 1

    while j < len(right_arr): 
        ret_l.append(right_arr[j])
        j += 1
    return ret_l

arr = list(range(0, 10))
random.shuffle(arr)
print(arr)
merge_sort(arr, start=0, end=len(arr))

