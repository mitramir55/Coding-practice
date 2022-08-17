# Bogo sort
# crazy!
import random
def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
        
    return arr

def is_sorted(arr):
    sum_ = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]: sum_+=1
    return sum_==len(arr)


arr = [1,2,0,5]
bogo_sort(arr=arr)

# experiment
is_sorted([1,2,0,5])
random.shuffle(arr)

arr

bogo_sort(arr=arr)