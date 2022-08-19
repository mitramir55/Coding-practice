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

# Time spent: 0.0209

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


start = time.time()
sum_array(arr1)
end = time.time()

print(f'Time spent: {end-start}')



# Time spent: 

def sum_array(arr):
    
    try:
        arr.remove(max(arr))
        arr.remove(min(arr))
        
        return sum(arr)
    
    except: return 0


start = time.time()
sum_array(arr1)
end = time.time()
print(f'Time spent: {end-start}')


#  Simple Encryption Series:
# Simple Encryption #1 - Alternating Split
'sdlfjsdkl'.isup


def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

solution('CadaverKiller')