
def findPeakUtil(arr, lowerBound, upperBound, n):
    
    
    # Find the middle index
    mid = lowerBound + (upperBound - lowerBound)/2
    mid = int(mid)
    print(f'mid ids = {mid} and value = {arr[mid]}')

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]): 
        print('return it!')
        return mid
        
    elif (mid > 0 and arr[mid + 1] > arr[mid]): 
        print('go to right...')
        return findPeakUtil(arr, (mid + 1), upperBound, n)
    else: 
        print('go to left...')
        return findPeakUtil(arr, lowerBound, (mid - 1), n)


arr = [10, 20, 23, 2, 1, 90, 67]
n = len(arr)
print("The peak point is", arr[findPeakUtil(arr, 0, n - 1, n)])

