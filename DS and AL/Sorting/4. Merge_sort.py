def swap(a, b):
    return b, a


def compare_and_merge(arr1, arr2):

    ret_list = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):

        # compare elements and add the smallest from each list
        if arr1[i] < arr2[j]: 
            ret_list.append(arr1[i])
            i+=1

        else:
            ret_list.append(arr2[j])
            j+=1

    # take care of the last element
    while i < len(arr1):
        ret_list.append(arr1[i])
        i+=1
        
    while j < len(arr2):
        ret_list.append(arr2[j])
        j+=1

    return ret_list


def merge_sort(arr):

    if len(arr)<2: return arr[:]
    
    mid = len(arr)//2
    left_sorted_half = merge_sort(arr[:mid])
    right_sorted_half = merge_sort(arr[mid:])

    return compare_and_merge(left_sorted_half, right_sorted_half)

arr = [2, 5, 3, 6, 8, 10]

merge_sort(arr)