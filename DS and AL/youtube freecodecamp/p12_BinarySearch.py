
# time and space complexity of this is Log(n)


arr = list(range(0, 10))
target = 9

def binary_search(target, s, e):

    mid_idx = s + (e - s)//2
    mid_val = arr[mid_idx]
    if mid_val == target: return ('found it!')

    if target > mid_val:
        print('go up!')
        return binary_search(target, s=mid_idx, e=e)
    else: 
        print('go down!')
        return binary_search(target, s=s, e=mid_idx)

binary_search(target, s=0, e=10)


#    REVIEW
# alternative version with space complexity of O(1)
# call is removed so we have no call stack

def binary_search_2(arr, target):
    e = len(arr) 
    s = 0

    while s < e:

        mid_idx = (e - s) // 2 + s
        print('mid_idx = ', mid_idx)

        if arr[mid_idx] == target: 
            return ('found it!')
        if arr[mid_idx] < target:
            print('go up')
            s = mid_idx + 1

        else: 
            print('go down!')
            e = mid_idx 

    return -1

binary_search_2(arr, target)