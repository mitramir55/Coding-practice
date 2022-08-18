import time

arr1 = [1, 2, 3, 5, 6, 8, 5, 9, 50]
arr2 = [1, 5, 6, 2, 8, 9, 6, 10 , 23]



# Time spent: 0.0378
start = time.time()

result = [i for i in arr1 if i not in arr2]

end = time.time()

print(f'Time spent: {end-start}')

# Time spent: 0.0410


start = time.time()

result = [i for i in arr1 if i not in set(arr2)]

end = time.time()

print(f'Time spent: {end-start}')



# Time spent: 


start = time.time()

x = set(arr2)
result = [i for i in arr1 if i not in x]

end = time.time()

print(f'Time spent: {end-start}')



# ---------------------
arr1 = [1,2,3,3]
arr1.remove(max(arr1))
arr1
