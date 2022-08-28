from cgitb import small


def quick_sort(arr):

    if len(arr) == 1 or len(arr) == 0: return arr
    pivot = arr[0]
    greater_vals = []
    smaller_vals = []

    for i in arr[1:]:
        if i > pivot: greater_vals.append(i)
        else: smaller_vals.append(i)

    return quick_sort(smaller_vals) + [pivot] + quick_sort(greater_vals)

arr = [5, 0, 60, 2, 5, 4, 3, 5]

quick_sort(arr)