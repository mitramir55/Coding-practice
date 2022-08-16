def funct_(prod):

    a = 1
    b = 1
    while a * b <=prod:
        prod_temp = a*b
        if prod_temp==prod:
            return [a, b, True]
        else:
            a, b = b, a+b
    return [a, b, False]

funct_(6)



def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

arr = [0, 1, 0, 1]

print("".join(map(str, arr)))

h = 0
a = 0
def cal(heads, legs):
    h = 0
    a = 0
    all_a = legs//4
    if all_a == heads: return h, all_a
    else:
        while heads!= h+a:
            a = all_a - 4
            h += 1
        return h, a
cal(heads=22, legs=72)


    return h, a