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


type(bin(-5))

'{:b}'.format(-5)
val1 = 5
val2 = 2
operation = '+'
round(eval("{0}{1}{2}{1}".format(round(val1), round(val2), operation)))

"{0}{1}{2}{1}".format(round(val1), round(val2), operation)


cc = "1"
'#' * (len(cc) - 4) + cc[-4:]

11%6


import math

prime_bigger_forty = [ i**2 + i + 41 for i in range(0, 40)]
prime_smaller_forty = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def is_prime(num):
    
    # eliminate less than 1
    if num <= 1: 
        return False
    
    num_sqrt = int(math.sqrt(num))

    if num in [2, 3]: return True

    # check primes less than 40
    for i in prime_smaller_forty: 

        if i <= num_sqrt:
            print('i = ', i)
            if num == i:
                return True
            
            # check if their devisable by any prime number
            elif num % i == 0: 
                return False
        else: break

    if num in prime_bigger_forty: return True

    # before checking the large numbers,
    # see if the square root is less than 40
    # if it is, then we've checked it before to make sure the number is not 
    # devisable by prime numbers < its sqrt 
    if num > 41 and num_sqrt < 41:
        return True


is_prime(num=73)







import math

prime_bigger_forty = [ i**2 + i + 41 for i in range(0, 40)]
prime_smaller_forty = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def is_prime(num):
    
    # eliminate less than 1
    if num <= 1: 
        return False
    
    num_sqrt = int(math.sqrt(num))

    if num in prime_smaller_forty + prime_bigger_forty: return True

    # check primes less than 40
    for i in prime_smaller_forty + prime_bigger_forty: 

        if i <= num_sqrt:
            print('i = ', i)
            
            # check if their devisable by any prime number
            if num % i == 0: 
                return False
        else: break

    # if the number was in none of those
    # start with 41 and go up two times
    dev = 41
    
    while dev <= num_sqrt:
        if num % dev ==0: 
            return False
        else: 
            dev += 2


    return True


is_prime(73)

num_sqrt = int(math.sqrt(num))

