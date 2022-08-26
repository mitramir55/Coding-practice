def swap(a, b):
    return b, a

def bubble_search(arr):

    swap_b = False

    while not swap_b:
        swap_b = True
        print('arr is = ', arr)

        # look at all n times
        for i in range(len(arr)-1):
            if not arr[i] < arr[i+1]: 
                arr[i], arr[i+1] = swap(arr[i], arr[i+1])
                swap_b = False
    return arr
            
arr = [2, 1, 0, 5, 3]

# worst case scenario n times
bubble_search(arr)